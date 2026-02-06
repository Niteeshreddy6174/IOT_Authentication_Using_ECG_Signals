#define SAMPLE_SIZE 100 // Adjust this based on the number of samples you want to process
#define ECG_PIN A0 // Analog pin connected to the ECG sensor
#define MAX_RUNTIME_MS 20000 // Maximum runtime in milliseconds (20 seconds)

int ecgData[SAMPLE_SIZE]; // Array to store raw ECG data

unsigned long startTime; // Variable to store the start time

void setup() {
  Serial.begin(9600);
  pinMode(ECG_PIN, INPUT);
  
  // Record the start time
  startTime = millis();
}

void loop() {
  // Check if the maximum runtime has been reached
  if (millis() - startTime >= MAX_RUNTIME_MS) {
    Serial.println("Exceeded maximum runtime. Stopping extraction.");
    while (true) {
      // Endless loop to stop further processing
    }
  }
  
  // Read raw ECG data
  for (int i = 0; i < SAMPLE_SIZE; i++) {
    ecgData[i] = analogRead(ECG_PIN);
    delay(10); // Adjust sampling frequency as needed
  }
  
  // Preprocess raw ECG data (basic preprocessing)
  for (int i = 0; i < SAMPLE_SIZE; i++) {
    // Apply median filtering (replace each value with the median of nearby values)
    ecgData[i] = applyMedianFilter(ecgData, i);
    
    // Normalize data to a range between 0 and 1023`
    ecgData[i] = map(ecgData[i], 0, 1023, 0, 1023);
  }
  
  // Send preprocessed ECG data over serial
  for (int i = 0; i < SAMPLE_SIZE; i++) {
    Serial.println(ecgData[i]);
  }
  
  // Add a delay before the next iteration
  delay(1000); // Adjust as needed
}

// Function to apply median filter to raw ECG data
int applyMedianFilter(int data[], int index) {
  // Calculate window size
  int windowSize = 5; // Adjust window size as needed
  
  // Create a temporary array to hold a window of data
  int window[windowSize];
  
  // Populate window
  for (int j = 0; j < windowSize; j++) {
    int windowIndex = index - (windowSize / 2) + j;
    if (windowIndex >= 0 && windowIndex < SAMPLE_SIZE) {
      window[j] = data[windowIndex];
    } else {
      window[j] = 0; // Zero-padding for edge cases
    }
  }

  // Sort window
  for (int j = 0; j < windowSize - 1; j++) {
    for (int k = j + 1; k < windowSize; k++) {
      if (window[j] > window[k]) {
        int temp = window[j];
        window[j] = window[k];
        window[k] = temp;
      }
    }
  }

  // Assign median value to result
  return window[windowSize / 2]; // Median value is at the middle index
}
