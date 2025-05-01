# Reddit-Sentiment-Analysis

## A. Description du Projet

- **Objectif :** Analyser en temps réel les sentiments exprimés dans des posts Reddit.
- **Pipeline :**

1. **Collecte des Données**  
   Le script `collect_reddit.py` se connecte à l'API Reddit grâce à PRAW, récupère des posts et les envoie à un topic Kafka nommé `reddit_topic`.

2. **Traitement en Streaming**  
   Le script `spark_streaming.py` lit en continu les messages du topic Kafka, nettoie le texte des posts (à l'aide de `data_cleaning.py`) et effectue une analyse de sentiment (via `sentiment_analysis.py` avec BERT).

## B. Prérequis

- **Logiciels :**
  - Python 3.x (par exemple, 3.12.8)
  - Apache Spark 3.x (avec Hadoop 3.x)
  - Apache Kafka 2.x
  - Java 8+
- **Librairies Python :**
  - praw, kafka-python, pyspark, matplotlib, pandas

## 4. Installation et Configuration

### 4.1. Installation d'Apache Kafka

- Télécharger Kafka depuis [le site officiel](https://kafka.apache.org/downloads) et l'extraire.
- Démarrer Zookeeper :
  bin/zookeeper-server-start.sh config/zookeeper.properties

- Démarrez Kafka :
  bin/kafka-server-start.sh config/server.properties

- Créez un topic Kafka nommé reddit_topic :
  bin/kafka-topics.sh --create --topic reddit_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

- Installer les dépendances :
  pip install -r requirements.txt

git clone https://github.com/hilary-tchokote/Reddit-Sentiment-Analysis.git
cd Reddit-Sentiment-Analysis


