## Ce script permet de traiter les posts Reddit en temps réel avec Spark Streaming.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, udf
from pyspark.sql.types import StructType, StringType, IntegerType, TimestampType
import sys
import os
import io

# Ajouter le répertoire parent au chemin pour les imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from data_cleaning import clean_posts
from sentiment_analysis import analyze_sentiment

# Forcer l'encodage UTF-8 pour les sorties console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("\u2705 Démarrage du streaming Spark...")

# Configuration de la session Spark
spark = SparkSession.builder \
    .appName("RedditSentimentAnalysis") \
    .master("local[*]") \
    .config("spark.hadoop.io.nativeio.enabled", "false") \
    .config("spark.hadoop.io.nativeio.useLegacyFileSystem", "true") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .config("spark.driver.extraJavaOptions", "-Djava.io.tmpdir=C:/temp") \
    .config("spark.executor.extraJavaOptions", "-Djava.io.tmpdir=C:/temp") \
    .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true") \
    .config("spark.sql.warehouse.dir", "file:///C:/temp/spark-warehouse") \
    .getOrCreate()


# Définition du schéma des tweets (correspondant aux données Kafka)
reddit_schema = StructType() \
    .add("keyword", StringType()) \
    .add("title", StringType()) \
    .add("text", StringType()) \
    .add("created_at", TimestampType()) \
    .add("upvotes", IntegerType()) \
    .add("num_comments", IntegerType()) \
    .add("author", StringType())

try:
    # Chargement des données depuis Kafka (lecture en streaming du topic 'reddit_topic')
    reddit_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "reddit_topic") \
        .load()

    # Conversion des données Kafka JSON -> DataFrame
    reddit_json = reddit_df.selectExpr("CAST(value AS STRING)")
    reddit_data = reddit_json.select(from_json(col("value"), reddit_schema).alias("data")).select("data.*")

    # Nettoyage du texte et analyse des sentiments
    clean_post_udf = udf(clean_posts, StringType())
    analyze_sentiment_udf = udf(lambda post: analyze_sentiment(post)['label'], StringType())

    reddit_cleaned = reddit_data.withColumn("cleaned_posts", clean_post_udf(col("text")))
    reddit_with_sentiment = reddit_cleaned.withColumn("sentiment", analyze_sentiment_udf(col("cleaned_posts")))
    
    # Définir le répertoire de checkpoint
    checkpoint_dir = "C:\sentiment-analysis-project\checkpoint"
    


    # Affichage du résultat dans la console
    query = reddit_with_sentiment.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()
        #.option("checkpointLocation", checkpoint_dir) \
        

    query.awaitTermination()

except Exception as e:
    print(f"❌ Erreur lors de l'exécution du streaming Spark : {e}")

finally:
    # Stopper la session Spark proprement
    spark.stop()
