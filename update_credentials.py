import os

def update_credentials():
    # Définir le chemin complet vers credentials.py
    credentials_path = os.path.join(
        os.path.expanduser("~"),
        "Documents",
        "SpotifyControllerApp",
        "Spotify",
        "credentials.py"
    )
    print("Fichier credentials trouvé à :", credentials_path)
    
    # Vérifier si le fichier existe
    if not os.path.exists(credentials_path):
        print("Erreur : Le fichier credentials.py n'a pas été trouvé.")
        return

    # Demander les nouvelles valeurs à l'utilisateur
    new_client_id = input("Entrez le nouveau SPOTIFY_CLIENT_ID : ").strip()
    new_client_secret = input("Entrez le nouveau SPOTIFY_CLIENT_SECRET : ").strip()
    
    # On peut demander le redirect_uri ou garder la valeur actuelle
    new_redirect_uri = input("Entrez le nouveau SPOTIFY_REDIRECT_URI (laisser vide pour conserver l'actuel) : ").strip()

    # Si l'utilisateur ne fournit pas de redirect_uri, lire la valeur actuelle depuis le fichier
    if not new_redirect_uri:
        try:
            with open(credentials_path, "r") as f:
                for line in f:
                    if "SPOTIFY_REDIRECT_URI" in line:
                        # On suppose une ligne du type : SPOTIFY_REDIRECT_URI = "http://localhost:8080"
                        parts = line.split("=")
                        if len(parts) >= 2:
                            current_value = parts[1].strip().strip('"').strip("'")
                            new_redirect_uri = current_value
                            break
            if not new_redirect_uri:
                new_redirect_uri = "http://localhost:8080"
        except Exception as e:
            print("Erreur lors de la lecture de SPOTIFY_REDIRECT_URI :", e)
            new_redirect_uri = "http://localhost:8080"
    
    # Construire le nouveau contenu du fichier
    new_content = f'''# credentials.py

SPOTIFY_CLIENT_ID = "{new_client_id}"
SPOTIFY_CLIENT_SECRET = "{new_client_secret}"
SPOTIFY_REDIRECT_URI = "{new_redirect_uri}"
'''

    # Écrire le nouveau contenu dans credentials.py
    try:
        with open(credentials_path, "w") as f:
            f.write(new_content)
        print("Les credentials ont été mis à jour avec succès.")
    except Exception as e:
        print("Erreur lors de l'écriture dans le fichier credentials.py :", e)

if __name__ == "__main__":
    update_credentials()
