% Example usage with ECG data from text files
fed_file_paths = {
    'C:\ECG project\matlab\fed files\fed_data_01.txt',
    'C:\ECG project\matlab\fed files\fed_data_02.txt',
    'C:\ECG project\matlab\fed files\fed_data_03.txt',
    'C:\ECG project\matlab\fed files\fed_data_04.txt',
    'C:\ECG project\matlab\fed files\fed_data_05.txt',
    'C:\ECG project\matlab\fed files\fed_data_06.txt',
    'C:\ECG project\matlab\fed files\fed_data_07.txt',
    'C:\ECG project\matlab\fed files\fed_data_08.txt',
    'C:\ECG project\matlab\fed files\fed_data_09.txt',
    'C:\ECG project\matlab\fed files\fed_data_10.txt'
};

default_input_file_location = 'C:\ECG project\matlab\input\';
input_file_name = input('Enter the name of the input text file: ', 's');
input_file_path = fullfile(default_input_file_location, input_file_name);

% Read the input ECG data from the text file
input_ecg_signal = read_ecg_data(input_file_path);

% Apply preprocessing steps (e.g., filtering, noise removal) to the input ECG signal
% Example: Applying a Butterworth bandpass filter
fs = 1000;      % Sampling frequency in Hz
lowcut = 0.5;   % Lower cutoff frequency in Hz
highcut = 40;   % Higher cutoff frequency in Hz
nyquist = 0.5 * fs;
[b, a] = butter(2, [lowcut, highcut] / nyquist, 'bandpass');
preprocessed_input_ecg = filtfilt(b, a, input_ecg_signal);

% Compare the preprocessed input ECG signal with each fed data file
match_found = false;
matched_file = '';

for i = 1:numel(fed_file_paths)
    fed_file_path = fed_file_paths{i};
    
    % Read the fed ECG data from the text file
    fed_ecg_signal = read_ecg_data(fed_file_path);
    
    % Apply the same preprocessing steps to the fed ECG signal as done for the input signal
    preprocessed_fed_ecg = filtfilt(b, a, fed_ecg_signal);
    
    % Compare the preprocessed input ECG signal with the preprocessed fed ECG signal
    similarity = dtw_compare_ecg(preprocessed_input_ecg, preprocessed_fed_ecg);
    
    % Set a threshold for similarity percentage
    threshold = 0.8;  % Example value, can be adjusted based on the distribution
    
    if similarity > threshold
        match_found = true;
        matched_file = fed_file_path;
        break;
    end
end

% Print the result based on the match status
if match_found
    disp(['Access granted. Matching file: ', matched_file]);
else
    disp('No access.');
end

% Read ECG data from text file
function ecg_data = read_ecg_data(file_path)
    data = load(file_path);
    ecg_data = data(:, 2);
end

function similarity = dtw_compare_ecg(ecg_signal_1, ecg_signal_2)
    % Dynamic Time Warping (DTW) to compare the preprocessed ECG signals
    dtw_distance = dtw(ecg_signal_1, ecg_signal_2);
    similarity = 1 / (1 + dtw_distance);
end
