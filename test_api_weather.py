import requests
import time
import datetime
import json

# Coordonnées de Paris
LATITUDE = 48.8566
LONGITUDE = 2.3522

# URL de l'API Open-Meteo
URL = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true"
)

def get_weather_data():
    """Récupère et affiche la météo actuelle à Paris."""
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        weather = data.get("current_weather", {})
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\n[{timestamp}] Météo actuelle à Paris :")
        print(json.dumps(weather, indent=2, ensure_ascii=False))

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération des données météo : {e}")

if __name__ == "__main__":
    print("🌦️  Démarrage du script météo (mise à jour toutes les 30 minutes)...")
    while True:
        get_weather_data()
        time.sleep(1800)  # 1800 secondes = 30 minutes
