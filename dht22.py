import adafruit_dht
import board
dht_device = adafruit_dht.DHT22(board.D4)
temperature = dht_device.temperature
humidity = dht_device.humidity
print("{0:0.1f} {1:0.1f}".format(temperature, humidity))

