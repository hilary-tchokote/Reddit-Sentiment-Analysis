## Ici, on stocke les posts Reddit dans MongoDB.

from pymongo import MongoClient
from kafka import KafkaConsumer
import json
import sys
import os
# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION, KEYWORDS
import time

# Authentification Twitter
#twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Connexion MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Configuration du consommateur Kafka
consumer = KafkaConsumer(
    'reddit_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='mongo-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📦 Enregistrement des posts Reddit dans MongoDB...")

#Inserer les données dans la base de données
for message in consumer:
    data = messsage.value
    collection.insert_one(data)
    print(f"✅ Post ajouté à MongoDB : {data['title']}")

