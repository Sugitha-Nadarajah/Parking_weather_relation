# Lien vers les datasets dispo : https://transport.data.gouv.fr/datasets/region/11?utm_source=chatgpt.com 
from configuration_access.config import API_KEY
import requests
import json
import time

CONTRACT = "lyon"  
URL = f"https://api.jcdecaux.com/vls/v1/stations?contract={CONTRACT}&apiKey={API_KEY}"

def get_bike_data():
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()  # Lève une erreur si le code != 200
        data = response.json()
        print(f"Nombre de stations : {len(data)}")
        print("Exemple de station :")
        print(json.dumps(data[0], indent=2, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print("❌ Erreur :", e)

# Boucle de test : récupère les données toutes les 30 min
if __name__ == "__main__":
    while True:
        print("\n--- Récupération des données JCDecaux ---")
        get_bike_data()
        time.sleep(1800)
