# 🚴‍♀️☁️ Real-Time Data Streaming with Kafka — JCDecaux Bikes & Weather

## 📌 Project Overview

This project demonstrates how to build a **real-time data pipeline** using **Apache Kafka**.  
Two external public APIs are used as data sources:

1. **JCDecaux API** — provides real-time information about bike stations (availability, locations, etc.).  
2. **Open-Meteo API** — provides real-time weather data for Paris.

The goal is to simulate a real DevOps-oriented workflow where streaming data from multiple sources is ingested, processed, and consumed continuously.

---
## ⚙️ Technologies Used

- 🐳 **Docker + Docker Compose** — for containerized Kafka & Zookeeper setup  
- 🦉 **Apache Kafka** — for real-time streaming and messaging  
- 🐍 **Python (Producers & Consumers)** — to fetch API data and push/read from Kafka  
- 🌦️ **Open-Meteo API** — public weather API (no auth required)  
- 🚲 **JCDecaux API** — real-time bike-sharing data (requires API key)  

---


