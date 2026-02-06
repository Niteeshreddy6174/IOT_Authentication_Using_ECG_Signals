import serial
import numpy as np
from scipy.signal import medfilt
import time

# Function to load and preprocess reference ECG data from text files
def load_reference_data(file_paths, fixed_length=None):
    reference_data = []
    
    # Load and preprocess each reference file
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = [int(line.strip()) for line in file.readlines() if line.strip()]
        
        # Apply median filtering for noise reduction
        data = medfilt(data, kernel_size=5)
        # Normalize data to have zero mean and unit variance
        data = (data - np.mean(data)) / np.std(data)
        
        reference_data.append(data)

    # Pad or truncate reference data arrays to fixed length if specified
    if fixed_length is not None:
        for i in range(len(reference_data)):
            ref_len = len(reference_data[i])
            if ref_len < fixed_length:
                # Pad with zeros
                reference_data[i] = np.pad(reference_data[i], (0, fixed_length - ref_len), mode='constant')
            elif ref_len > fixed_length:
                # Truncate
                reference_data[i] = reference_data[i][:fixed_length]

    return np.array(reference_data)

# Function to preprocess live ECG data received from Arduino
def preprocess_live_data(live_data, fixed_length):
    live_data_len = len(live_data)
    if live_data_len < fixed_length:
        # Pad with zeros
        live_data = np.pad(live_data, (0, fixed_length - live_data_len), mode='constant')
    elif live_data_len > fixed_length:
        # Truncate
        live_data = live_data[:fixed_length]
    # Apply median filtering for noise reduction
    live_data = medfilt(live_data, kernel_size=5)
    # Normalize live data to have zero mean and unit variance
    live_data = (live_data - np.mean(live_data)) / np.std(live_data)
    return live_data

# Function to compare live ECG data with reference data and perform authentication
def authenticate_live_data(live_data, reference_data, threshold=0.80):
    # Calculate similarity score (e.g., correlation coefficient) between live and reference data
    similarity_scores = [np.corrcoef(live_data, ref_data)[0, 1] for ref_data in reference_data]
    max_similarity_score = max(similarity_scores)

    # Authenticate based on similarity score
    if max_similarity_score > threshold:
        return True
    else:
        return False

if __name__ == "__main__":
    # Set the COM port for serial communication
    port = 'COM5'  # Adjust this to match the actual COM port of your Arduino
    baudrate = 9600  # Adjust baudrate as needed

    # List of reference data file paths
    reference_file_paths = ["p1.txt", "p2.txt", "p3.txt"]  # Add more file paths as needed

    # Load and preprocess reference ECG data
    reference_data = load_reference_data(reference_file_paths, fixed_length=1000)

    # Open serial connection to Arduino
    try:
        ser = serial.Serial(port, baudrate)
        print("Serial connection established with", port)
    except serial.SerialException:
        print("Failed to open serial port. Please check the port configuration.")
        exit()

    # Read live ECG data from Arduino for up to 20 seconds
    start_time = time.time()
    live_data = []
    while time.time() - start_time < 20:
        try:
            line = ser.readline().strip()
            if line.isdigit():
                data_point = int(line)
                live_data.append(data_point)
                print("Received data point:", data_point)
        except ValueError:
            pass

    # If no data points are received, prompt the user to check the Arduino setup
    if not live_data:
        print("Error: No data received from Arduino. Please check the Arduino setup.")
        exit()

    # Preprocess live data
    live_data = preprocess_live_data(live_data, fixed_length=1000)

    # Authenticate live data
    if authenticate_live_data(live_data, reference_data):
        print("Authentication successful. Access granted.")
    else:
        print("Authentication failed. Access denied.")

    # Close serial connection
    ser.close()
