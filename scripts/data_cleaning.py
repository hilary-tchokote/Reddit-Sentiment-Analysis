import re

# Fonction pour nettoyer les posts
def clean_posts(post): 
    """
    Nettoie le texte d'un post en supprimant les mentions, liens, hashtags, etc.
    """
    post = re.sub(r'@[A-Za-z0-9]+', '', post)  # Supprimer les mentions (@user)
    post = re.sub(r'http\S+', '', post)  # Supprimer les liens
    post = re.sub(r'#', '', post)  # Supprimer le caractère 
    post = re.sub(r'RT[\s]+', '', post)  # Supprimer les reposts
    post = re.sub(r'\s+', ' ', post).strip() # Remplacer les espaces multiples par un seul espace
    post = re.sub(r'[^\w\s]', '', post)  # Supprimer la ponctuation	
    return post.lower()  # Convertir en minuscules


# Test du nettoyage
if __name__ == "__main__":
    post = "@user Voici un super lien http://example.com #BigData 🚀 RT"
    print("post original :", post)
    print("post nettoyé  :", clean_post(post))


