import time
import board
import busio
import adafruit_ahtx0
import csv
import math

def capture_humidity_data():
    
	#Define pins 27(SDA)/28(SCL) on the jetson nano for i2c communication
	scl = board.SCL_1
	sda = board.SDA_1

	#establish connection with AHT10 sensor using i2c Bus 0
	i2c = busio.I2C(scl,sda)
	sensor = adafruit_ahtx0.AHTx0(i2c)

    	# Create a CSV file and write headers
	csv_file = open('humidity_data.csv', 'w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['Timestamp', 'Humidity' , 'Air Temp (C)' , 'VPD'])

	while True:
        	# Read humidity & Temperature data from the DHT22 sensor
		humidity = sensor.relative_humidity
		print("RH   (%):",humidity)
		temperature = sensor.temperature
		print("Temp (C):",temperature)
		

		# Calculate the environmental VPD
		saturation_vapor_pressure = 0.611 * math.exp((17.27 * temperature) / (temperature + 237.3))
		actual_vapor_pressure = saturation_vapor_pressure * (humidity / 100)
		vpd_env = saturation_vapor_pressure - actual_vapor_pressure

		if humidity is not None:
			# Get the current timestamp
			timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

			# Write the timestamp and humidity to the CSV file
			csv_writer.writerow([timestamp, humidity, temperature, vpd_env ])
			csv_file.flush()

		# Wait for a few seconds before reading again
		time.sleep(2)

	# Close the CSV file
	csv_file.close()

if __name__ == '__main__':
    	capture_humidity_data()
