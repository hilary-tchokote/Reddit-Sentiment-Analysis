## Ici, on récupère les posts Reddit selon des mots-clés et les envoie vers Kafka.

import praw
from kafka import KafkaProducer
import json
import sys
import os
import time

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import KEYWORDS, CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD, KAFKA_BROKER, KAFKA_TOPIC

# Authentification Reddit
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD
)

# Connexion Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Fonction pour collecter les tweets récents
def collect_reddit_posts(keywords, limit=100):
    try:
        for keyword in keywords:
            print(f"🔍 Recherche des posts pour le mot-clé : {keyword}")
            for submission in reddit.subreddit("all").search(keyword, limit=limit):
                data = {
                        "keyword": keyword,
                        "title": submission.title,
                        "text": submission.selftext,
                        "created_at": submission.created_utc,
                        "upvotes": submission.score,
                        "num_comments": submission.num_comments,
                        "author": str(submission.author)
                }
                producer.send("reddit_topic", value=data)
                print(f"✅ Post envoyé : {data['title']}")
                time.sleep(2)

    except Exception as e: 
        print(f"❌ Erreur lors de la récupération des posts : {e}")
        # except tweepy.errors.TooManyRequests:
        #     print("Trop de requêtes ! Pause de 15 minutes...")
        #     time.sleep(15 * 60)  # Pause pendant 15 minutes
        #     collect_tweets(query, count)
    
    

# Lancer la collecte
if __name__ == "__main__":
    print("Authentification réussie, collecte des posts...")
    collect_reddit_posts(KEYWORDS, 100)

