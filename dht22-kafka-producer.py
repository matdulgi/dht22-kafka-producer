import sys
import adafruit_dht
import board
import time
import traceback
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['pi1:9092', 'pi2:9092', 'pi3:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

dht_device = adafruit_dht.DHT22(board.D4)

while True:
  try:
    temp= dht_device.temperature
    hum= dht_device.humidity
    
#    data = "{0:0.1f} {1:0.1f} {2}".format(temp, hum, str(time.time()))
    json_object = {
        "temperature": temp,
        "humidity": hum,
        "timestamp": str(time.time())
    }

#  print("{0:0.1f} {1:0.1f}".format(temperature, humidity))
    producer.send('dht22', value=json_object)
    producer.flush()
    time.sleep(5)
  except RuntimeError as re:
    traceback.print_exc()
    

