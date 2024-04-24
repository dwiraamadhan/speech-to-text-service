from confluent_kafka import Producer
import socket


# create function to send transcription to kafka
def send_to_kafka(message):
    # kafka configuration
    conf = {
    "bootstrap.servers" : "localhost:9092",
    "client.id" : socket.gethostname()
    }

    # create object producer kafka
    producer = Producer(conf)

    # function for delivery report kafka to check if message delivered or not
    def delivery_report(err, msg):
        if err is not None:
            print('Message delivery failed: %s' % err)
        else:
            print('Message delivered to %s [%d]' % (msg.topic(), msg.partition()))

    # send transcription to kafka
    producer.produce(topic="topicPertama", value=message, callback=delivery_report)
    producer.flush()

