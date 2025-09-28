from kafka import KafkaConsumer

# Set up the Kafka consumer
consumer = KafkaConsumer(
    'payment-transactions',
    group_id='my-group',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest'
)

# Poll messages from the topic
for message in consumer:
    print(f"Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}")
    print(f"Key: {message.key}, Value: {message.value.decode('utf-8')}")
