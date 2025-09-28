# 🚀 Set Up Kafka Cluster with Systemd & Kafdrop UI

This project provides a step-by-step guide to **set up Apache Kafka** on a Linux server with **systemd services** for easy management, and **Kafdrop** for a simple web UI.  

Kafka is widely used for **scalable data streaming** and **real-time event processing**.

---

## 📑 Table of Contents
1. [Prerequisites](#-prerequisites)
2. [Install Java](#-install-java)
3. [Download & Extract Kafka](#-download--extract-kafka)
4. [Create ZooKeeper Service](#-create-zookeeper-service)
5. [Create Kafka Service](#-create-kafka-service)
6. [Start Kafka & ZooKeeper](#-start-kafka--zookeeper)
7. [Install Kafdrop (Kafka UI)](#-install-kafdrop-kafka-ui)
8. [Start Kafdrop Service](#-start-kafdrop-service)
9. [Access the UI](#-access-the-ui)

## ✅ Prerequisites
Make sure you have the following installed on your system:

- `curl` → for downloading Kafka  
- `tar` → for extracting Kafka archives  
- `systemd` → for managing services  
- `Java` (required by Kafka)  

## 🔧 Install Java
Kafka requires Java. In this setup, we’ll use **Java 17**:
```bash
sudo apt update && sudo apt install -y openjdk-17-jdk
```

## 📦 Download & Extract Kafka
Download Kafka 3.7.1 (latest at the time of writing). Check Apache Kafka Downloads for newer versions.
```bash
curl -L https://downloads.apache.org/kafka/3.7.1/kafka_2.13-3.7.1.tgz -o kafka.tgz
sudo mkdir -p /opt/kafka
tar -xvzf kafka.tgz --strip 1 -C /opt/kafka
```

## 🦓 Create ZooKeeper Service
Kafka requires ZooKeeper (until KRaft mode fully replaces it).

Create a systemd unit file:
```bash
sudo vi /etc/systemd/system/zookeeper.service
```
Paste the following:
```ini
[Unit]
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
User=root
ExecStart=/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
ExecStop=/opt/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

## 🐦 Create Kafka Service
Now create a service for Kafka:
```bash
sudo vi /etc/systemd/system/kafka.service
```
Paste the following:
```ini
[Unit]
Requires=zookeeper.service
After=zookeeper.service

[Service]
Type=simple
User=root
ExecStart=/bin/sh -c '/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties > /opt/kafka/kafka.log 2>&1'
ExecStop=/opt/kafka/bin/kafka-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

## 🟢 Start Kafka & ZooKeeper
```bash
sudo systemctl enable zookeeper
sudo systemctl start zookeeper
sudo systemctl enable kafka
sudo systemctl start kafka
```
Check status with:
```bash
systemctl status zookeeper
systemctl status kafka
```

## 🌐 Install Kafdrop (Kafka UI)
Kafdrop is a lightweight web UI for Kafka.

Download the latest .jar file:
```bash
sudo curl -L https://github.com/obsidiandynamics/kafdrop/releases/download/4.0.2/kafdrop-4.0.2.jar -o /opt/kafdrop-4.0.2.jar
```
## 🟢 Start Kafdrop Service
Create a systemd service for Kafdrop:
```bash
sudo vi /etc/systemd/system/kafkaui.service
```
Paste the following:
```ini
[Unit]
Description=Web UI for administration of Kafka clusters
Requires=kafka.service
After=kafka.service

[Service]
User=root
WorkingDirectory=/opt/
ExecStart=/usr/bin/java --add-opens=java.base/sun.nio.ch=ALL-UNNAMED -jar kafdrop-4.0.2.jar --kafka.brokerConnect=ubuntu-host:9092
StartLimitInterval=0
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```
Enable and start the service:
```bash
sudo systemctl enable kafkaui.service
sudo systemctl start kafkaui.service
```
## 🌍 Access the UI
Once started, open your browser and navigate to:
```
http://<your-server-ip>:9000
```
You should now see the Kafdrop Web UI where you can explore topics, consumers, and messages.
