import serial
import csv
import time
from datetime import datetime
red=0
# Replace 'COMx' with your actual COM port name and set the baud rate accordingly.
ser = serial.Serial('COM68', baudrate=115200)

# Create a CSV file and write the header
csv_file = open('com_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

try:
    while True:
        
        # Read data from the COM port
        data = ser.readline().decode()
        red+=1
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("reading done",red)
        # Write the data and timestamp to the CSV file
        csv_writer.writerow([timestamp, data])
        csv_file.flush()
        
        # Wait for 1 minute
        print(data)
        
        
except KeyboardInterrupt:
    print("Data collection stopped by the user.")

finally:
    # Close the CSV file and the COM port when done
    csv_file.close()
    ser.close()
