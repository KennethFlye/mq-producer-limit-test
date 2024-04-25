import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='clear', exchange_type='fanout')

message = "Clear Sensor Table"
channel.basic_publish(exchange='clear', routing_key='', body=message)
print(f" Producer Sent: {message}")
connection.close()