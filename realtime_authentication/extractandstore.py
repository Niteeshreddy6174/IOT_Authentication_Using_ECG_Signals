import serial
import time

# Set the COM port for serial communication
port = 'COM5'  # Adjust this to match the actual COM port of your Arduino
baudrate = 9600  # Adjust baudrate as needed

# Set the file path to save the data
file_path = "p1.txt"  # Adjust this to your desired file path and name

# Set maximum runtime in seconds
MAX_RUNTIME_SEC = 20

# Set the target length of data points to extract
TARGET_LENGTH = 1000

# Open the serial connection
try:
    ser = serial.Serial(port, baudrate)
    print("Serial connection established with", port)
except serial.SerialException:
    print("Failed to open serial port. Please check the port configuration.")
    exit()

# Open the file to save the data
with open(file_path, 'w') as file:
    start_time = time.time()  # Record the start time
    data_points_count = 0  # Initialize counter for data points received
    while True:
        # Check if maximum runtime has been reached
        if time.time() - start_time >= MAX_RUNTIME_SEC:
            print("Exceeded maximum runtime. Stopping extraction.")
            break

        data = ser.readline().decode().strip()  # Read data from serial port
        if data == "Exceeded maximum runtime. Stopping extraction.":
            break  # Stop reading if end message is received

        file.write(data + '\n')  # Write raw data to file
        data_points_count += 1  # Increment counter for data points received
        print("Received data point:", data)  # Print data point to console (optional)

        # Check if target length of data points has been reached
        if data_points_count >= TARGET_LENGTH:
            print("Target length of data points reached. Stopping extraction.")
            break

# Close the serial connection
ser.close()
