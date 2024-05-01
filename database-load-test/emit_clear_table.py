import pika
import configparser

config = configparser.ConfigParser()

config.read(r'config/settings/config.ini')

mq_server_host = config.get("MQ", "mq_server_host")
mq_user = config.get("MQ", "mq_user")
mq_password = config.get("MQ", "mq_password")
credentials = pika.PlainCredentials(mq_user, mq_password)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='clear', exchange_type='fanout')

message = "Clear Sensor Table"
channel.basic_publish(exchange='clear', routing_key='', body=message)
print(f" Producer Sent: {message}")
connection.close()