## Ici, on utilise le modèle BERT pour analyser les sentiments

from transformers import pipeline

# Charger le modèle BERT pour l'analyse des sentiments
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(post, neutral_threshold=0.6):
    """
    Analyse le sentiment d'un texte donné.
    Labels possibles : POSITIVE, NEGATIVE, NEUTRAL.
    - neutral_threshold : seuil pour considérer un post comme neutre.
    """
    if not post.strip():
        return {"label": "NEUTRAL", "score": 0.0}

    result = sentiment_pipeline(post[:512])[0]
    label = result['label']
    score = result['score']

    # Définir un label "NEUTRAL" si le score est proche de l'équilibre
    if label == "POSITIVE" and score < neutral_threshold:
        label = "NEUTRAL"
    elif label == "NEGATIVE" and score < neutral_threshold:
        label = "NEUTRAL"

    return {"label": label, "score": score}

# Test rapide
if __name__ == "__main__":
    sample_posts = [
        "Je suis ravi de ce projet, c'est génial ! 🎉",
        "C'est la pire expérience que j'ai jamais eue...",
        "Je suis juste neutre par rapport à cette situation."
    ]
    
    for post in sample_posts:
        print(f"post : {post}")
        print("Analyse des sentiments :", analyze_sentiment(post))
