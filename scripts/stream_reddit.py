## Ce script permet de récupèrer les posts depuis Kafka et les affiche en temps réel.
from kafka import KafkaConsumer
import json

# Configuration du consommateur Kafka
consumer = KafkaConsumer(
    'reddit_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='reddit-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📡 En attente des données Reddit...")

# Écoute les posts Reddit depuis Kafka
for message in consumer:
    data = message.value
    print(f"🔸 Nouveau post : {data['title']} | {data['text'][:100]}...")


