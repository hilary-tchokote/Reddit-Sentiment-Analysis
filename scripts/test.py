
import praw
import sys
import os
import time

# Ajouter le répertoire parent au chemin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

try:
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD
    )
    print(f"Authentification réussie en tant que : {reddit.user.me()}")

    # Test de récupération de posts
    for submission in reddit.subreddit("all").search("Big Data", limit=5):
        print(f"Titre : {submission.title}, Auteur : {submission.author}")

except Exception as e:
    print(f"Erreur : {e}")

    