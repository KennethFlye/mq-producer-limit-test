import pika, sys, uuid
import configparser

config = configparser.ConfigParser()

config.read(r'src/config/settings/config.ini')

mq_server_host = config.get("MQ", "mq_server_host")
mq_user = config.get("MQ", "mq_user")
mq_password = config.get("MQ", "mq_password")
credentials = pika.PlainCredentials(mq_user, mq_password)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='write', exchange_type='fanout')

message = str(uuid.uuid4())
channel.basic_publish(exchange='write', routing_key='', body=message)
print(f" Producer Sent: {message}")
connection.close()