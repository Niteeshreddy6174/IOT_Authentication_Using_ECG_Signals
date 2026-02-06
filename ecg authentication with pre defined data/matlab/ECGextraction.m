% Define the output text file name
outputFile = 'output_data.txt';

% Set the sampling rate and duration
samplingRate = 1000; % Sampling rate in Hz
duration = 10; % Duration of data collection in seconds

% Create an analog input object for ECG data acquisition
ai = analoginput('winsound');
addchannel(ai, 1);

% Set the acquisition parameters
set(ai, 'SampleRate', samplingRate);
set(ai, 'SamplesPerTrigger', duration * samplingRate);

% Open the output file for writing
fid_out = fopen(outputFile, 'w');

% Start the data acquisition
start(ai);

% Collect and process the real-time data
while ai.SamplesAcquired < duration * samplingRate
    % Wait for the acquisition to complete
    while ai.SamplesAcquired < ai.SamplesPerTrigger
        pause(0.1);
    end
    
    % Read the acquired ECG data
    ecgData = getdata(ai);
    
    % Process the acquired ECG data
    % Replace this section with your desired processing algorithm

    % Example: Save the processed data in the output file
    for i = 1:length(ecgData)
        processedData = ecgData(i) * 2; % Example processing: scaling the data by 2
        fprintf(fid_out, '%f\n', processedData);
    end
end

% Stop the data acquisition
stop(ai);

% Close the output file
fclose(fid_out);

% Display a message when the processing is complete
disp('Real-time data processing completed and saved to output file.');
