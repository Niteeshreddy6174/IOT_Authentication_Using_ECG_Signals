import time

# Define the input ECG file name
input_file = 'Person_19.txt'

# Define the output text file name
output_file = 'Processed_Person_19.txt'

try:
    # Open the input file for reading
    with open(input_file, 'r') as f:
        ecg_data = f.readlines()
        ecg_data = [float(data.split(',')[1].strip()) for data in ecg_data]  # Assuming the ECG value is the second element after splitting by comma

    # Open the output file for writing
    with open(output_file, 'w') as f_out:
        # Perform real-time processing on the ECG data
        # Replace this section with your desired processing algorithm

        # Example: Save the processed data in the output file
        for data in ecg_data:
            processed_data = data * 2  # Example processing: scaling the data by 2
            f_out.write(f'{data},{processed_data}\n')  # Writing both original and processed data
            # time.sleep(0.1)  # Simulate real-time processing delay (adjust as needed)

    # Display a message when the processing is complete
    print('Real-time data processing completed and saved to output file.')

except Exception as e:
    print(f"An error occurred: {str(e)}")
