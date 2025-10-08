from kafka import KafkaProducer
import requests, json, time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

URL = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&current_weather=true"

while True:
    data = requests.get(URL).json()
    weather = data["current_weather"]
    producer.send("weather_paris", weather)
    print("✅ Message envoyé :", weather)
    time.sleep(1800)
    
    
    """ Producer role:
    - calls the Open-Meteo API
    - retrieves the weather (temperature, wind, etc.)
    - sends this data to a Kafka topic named, for example, weather_paris
    """