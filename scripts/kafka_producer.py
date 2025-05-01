## Ce script envoie les données Reddit à Kafka.
from kafka import KafkaProducer
import json
import sys
import os
#import time

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import KEYWORDS
from collect_reddit import collect_reddit_posts

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_reddit_posts():
    posts = collect_reddit_posts(KEYWORDS, limit=100)
    for post in posts:
        producer.send('reddit_topic', value=post)
        print(f"Post envoyé : {post['title']}")

if __name__ == "__main__":
    produce_reddit_posts()



