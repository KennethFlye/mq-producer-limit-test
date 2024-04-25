import pika, sys, uuid

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='write', exchange_type='fanout')

message = str(uuid.uuid4())
channel.basic_publish(exchange='write', routing_key='', body=message)
print(f" Producer Sent: {message}")
connection.close()