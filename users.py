import json
from datetime import datetime


FILENAME = "players.json"

# Charger les données depuis le fichier JSON, ou initialiser si le fichier n'existe pas
def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Sauvegarder les données dans le fichier JSON
def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

# Vérifier si un joueur est déjà inscrit dans le fichier
def is_player_registered(player_name):
    data = load_data()
    return player_name in data

# Inscrire un joueur s'il n'est pas déjà enregistré
def register_player(player_name):
    data = load_data()
    if not is_player_registered(player_name):
        data[player_name] = []
        save_data(data)
        print(f"Le joueur '{player_name}' a été inscrit.\n")
    else:
        print(f"Le joueur '{player_name}' est déjà inscrit.")

# Afficher l'historique des scores d'un joueur
def display_scores(player_name):
    data = load_data()
    if is_player_registered(player_name):
        scores = data[player_name]
        if scores:
            print(f"Historique des scores pour '{player_name}':")
            for entry in scores:
                print(f"- Date: {entry['date']}, Score: {entry['score']} {entry['category']}")
        else:
            print(f"Aucun score enregistré pour '{player_name}'.")
    else:
        print(f"Le joueur '{player_name}' n'est pas inscrit.")

# Ajouter un score pour un joueur
def add_score(player_name, score,category):
    data = load_data()
    if is_player_registered(player_name):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data[player_name].append({"date": date, "score": score,"category":category})
        save_data(data)
        print(f"\nScore de {score} ajouté pour '{player_name}' dans {category} le {date}.")
    else:
        print(f"Le joueur '{player_name}' n'est pas inscrit. Veuillez l'inscrire d'abord.")


