from confluent_kafka import Producer, KafkaError
import socket, os

def check_kafka_connection():
    try:
        # kafka configuration
        conf = {
            "bootstrap.servers" : os.getenv("BROKER_SERVER"),
            "client.id" : socket.gethostname(),
        }

        # check connection kafka with getting list of topics
        producer = Producer(conf)
        producer.list_topics()
        print("Successfully connected to Kafka using Producer!")

        return True

    except Exception as e:
        print(f"Failed to connect to Kafka server: {e}")
        return False
    