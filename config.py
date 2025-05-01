import os 
from dotenv import load_dotenv

# Load environment variables
#load_dotenv()
load_dotenv(dotenv_path="c:/Users/Hilary/Desktop/sentiment-analysis-project/.env")




# Twitter API
# BEARER_TOKEN = os.getenv("BEARER_TOKEN")
# API_KEY = os.getenv("API_KEY")
# API_KEY_SECRET = os.getenv("API_KEY_SECRET")
# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

#print("BEARER_TOKEN:", BEARER_TOKEN)

#Reddit API KEYS
CLIENT_ID = "Hi6RrmlLf2-ZaB2vHFwcZQ"
CLIENT_SECRET = "Op-iLCKw1gCfIf4qKvrq1qb-PcRteA"
USER_AGENT = "sentiment-analysis-project by /u/SimilarLavishness323"
USERNAME = "SimilarLavishness323"
PASSWORD = "Reddit&25"

# CLIENT_ID = os.getenv("CLIENT_ID")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")    
# USER_AGENT = os.getenv("USER_AGENT")
# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PASSWORD")

print("CLIENT_ID:", CLIENT_ID)

# MongoDB (local)
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Kafka
KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

# Key word for the straming
KEYWORDS = ["Big Data", "Python", "Data Analysis", "Data Visualisation", "API"]
LANGUAGES = ["fr"]

