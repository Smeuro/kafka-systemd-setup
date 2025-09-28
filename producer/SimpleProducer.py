from kafka import KafkaProducer
from kafka.errors import KafkaError

def on_send_success(record_metadata):
    print(f"Message sent to topic: {record_metadata.topic}, partition: {record_metadata.partition}, offset: {record_metadata.offset}")

def on_send_error(excp):
    print(f"Error while producing message: {excp}")

def main():
    # Kafka configuration
    kafka_config = {
        'bootstrap_servers': 'localhost:9092',
        'key_serializer': str.encode,
        'value_serializer': str.encode
    }

    # Create Kafka producer
    producer = KafkaProducer(**kafka_config)

    # Send the message to the "payment-transactions" Kafka topic
    topic_name = "payment-transactions"
    message_key = "transactionKey"
    message_value = "Payment processed successfully"

    # Produce the message with error handling
    producer.send(topic_name, key=message_key, value=message_value).add_callback(on_send_success).add_errback(on_send_error)

    # Wait for all messages to be sent
    producer.flush()

if __name__ == "__main__":
    main()
