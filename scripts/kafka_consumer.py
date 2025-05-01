from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'reddit_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='reddit-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consommation des posts Reddit...")

for message in consumer:
    print(f"Post reçu : {message.value['title']}")


