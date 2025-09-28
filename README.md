# 🚀 Kafka Python Project

This project demonstrates how to set up **Apache Kafka** on Linux with `systemd`, 
and how to create simple **Producer** and **Consumer** apps in Python.

## 📑 Project Structure
- [setup/KAFKA_SETUP.md](setup/KAFKA_SETUP.md) → Kafka & systemd setup guide
- [producer/SimpleProducer.py](producer/SimpleProducer.py) → Kafka Producer
- [consumer/SimpleConsumer.py](consumer/SimpleConsumer.py) → Kafka Consumer

## 🔧 Requirements
Install dependencies:
```bash
pip install -r requirements.txt
```
## 🚀 Run
1. Start Kafka & ZooKeeper (see setup guide).
2. Run producer:
```bash
python3 producer/SimpleProducer.py
```
3. Run consumer
```bash
python3 consumer/SimpleConsumer.py
```
