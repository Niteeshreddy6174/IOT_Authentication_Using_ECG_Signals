Markdown
# Real-Time ECG Biometric Authentication System 🫀🔐

![Status](https://img.shields.io/badge/Status-Completed-success)
![Platform](https://img.shields.io/badge/Platform-Arduino%20%7C%20Python-blue)
![Domain](https://img.shields.io/badge/Domain-IoT%20%26%20Biometrics-red)

> **A novel biometric security system that authenticates users based on their unique cardiac rhythm (Electrocardiogram) using Signal Processing and Machine Learning concepts.**

---

## 📖 Overview

Passwords can be stolen, and fingerprints can be forged. This project introduces **ECG Biometric Authentication**—a system that uses the unique electrical activity of the human heart to verify identity.

Leveraging an **Arduino Uno** for data acquisition and **Python** for complex signal processing, this system captures real-time ECG data, filters noise, and compares it against a secure database of reference signals using statistical correlation.

**Key Metrics:**
* [cite_start]**Accuracy:** ~95% in simulated scenarios[cite: 286].
* [cite_start]**Processing Time:** ~0.5 seconds per segment[cite: 285].
* [cite_start]**Sampling Rate:** 250 Hz[cite: 277].

---

## 🌟 Key Features

* [cite_start]**Real-Time Acquisition:** Live streaming of cardiac data from the AD8232 sensor to Python via Serial communication[cite: 277].
* [cite_start]**Signal Preprocessing:** Implementation of **Median Filtering (Kernel size: 5)** to remove baseline wander and muscle artifacts[cite: 278].
* [cite_start]**Dynamic Normalization:** Standardizes signal amplitudes to ensuring accurate comparison regardless of sensor contact pressure[cite: 278].
* [cite_start]**Correlation Algorithm:** Uses **Pearson Correlation Coefficients** to determine similarity scores with a strict threshold of **0.80**[cite: 280].
* [cite_start]**Instant Feedback:** Real-time "Access Granted" or "Access Denied" visualization[cite: 284].

---

## 🛠️ Tech Stack & Hardware

### Hardware Components
| Component | Specification | Function |
| :--- | :--- | :--- |
| **Microcontroller** | Arduino Uno (ATmega328P) | [cite_start]Analog-to-Digital conversion & transmission [cite: 263] |
| **Sensor** | AD8232 Heart Rate Monitor | [cite_start]Captures bio-potential signals of the heart [cite: 265] |
| **Electrodes** | Standard ECG Pads | [cite_start]3-Lead placement (RA, LA, RL) [cite: 267] |
| **Connection** | USB / Serial | Data transmission to PC |

### Software & Libraries
* **Firmware:** Arduino IDE (C++)
* **Processing Core:** Python 3.x
* **Libraries:**
    * `pyserial` (Data transmission)
    * `numpy` (Numerical operations)
    * [cite_start]`scipy` (Signal filtering - `medfilt`) [cite: 357]

---

## ⚙️ Circuit Connection

[cite_start]Connect the AD8232 Sensor to the Arduino Uno as follows[cite: 247, 248]:

| AD8232 Pin | Arduino Pin |
| :--- | :--- |
| **GND** | GND |
| **3.3V** | 3.3V |
| **OUTPUT** | A0 (Analog 0) |
| **LO-** | Digital 11 |
| **LO+** | Digital 10 |

[cite_start]*(Note: Ensure electrodes are placed correctly: Red (RA), Yellow (LA), Green (RL/Ground) for optimal signal clarity.)* [cite: 288]

---

## 🚀 Installation & Usage

### 1. Hardware Setup
Assemble the circuit as per the table above. Connect the Arduino to your PC via USB.

### 2. Arduino Firmware
1. Open `ECG_Acquisition.ino` (Create this from your report code).
2. Select the correct **COM Port** and **Board** in Arduino IDE.
3. Upload the code.

### 3. Python Environment
Install the required dependencies:
```bash
pip install pyserial numpy scipy
4. Running the System
Step A: Enroll a User (Create Reference) Run the extraction script to save your unique heart signature.

Bash
python data_extraction.py
This will save p1.txt containing your raw ECG data.

Step B: Authenticate Run the main authentication script.

Bash
python authentication.py
The system will listen to the live sensor feed, compare it with p1.txt, and grant or deny access.

🧠 How It Works (The Algorithm)
Data Ingestion: The system captures 1000 data points at 250Hz.


Noise Reduction: A median filter smooths the wave, removing spikes caused by movement.


Normalization: (Data - Mean) / Std_Dev makes the wave scale-invariant.

Pattern Matching: The live wave is compared to the stored wave.

Decision Logic:

Python
if correlation_score > 0.80:
    return "Access Granted"
else:
    return "Access Denied"
📈 Results
The system was tested under various conditions, including baseline wander and electrode displacement.

Success Rate: Accurately flagged non-authentic signals with scores dropping significantly below the 0.80 threshold.

Visualization: Below is an example of the filtered signal vs. original signal.

(Place the image from Figure 3.1 or Page 7 of your PDF here)

🔮 Future Improvements

Multi-Lead Support: Integrating 12-lead ECG for medical-grade accuracy.


Deep Learning: Replacing correlation with CNNs (Convolutional Neural Networks) for feature extraction.


Cloud Integration: Storing biometric profiles on a secure cloud server for remote authentication.


Wearable Integration: Porting the code to low-power ESP32 modules for smartwatch integration.

📜 License & Acknowledgments
This project was developed as part of the IoT Domain Analyst (BECE352E) course at VIT Chennai.

Credits:


Developer: Niteesh Kumar Reddy / Aalla Srideep 


Guide: Dr. Manigandan M 


### 💡 Suggestions to make your Repo look even better:
1.  **Upload the Images:** Take the screenshots from your PDF (like the "Connection Diagram" on Page 5 and the "Filtered Signal" graph on Page 7) and save them as images (e.g., `schematic.png`, `signal_graph.png`) in your GitHub folder.
2.  **Add the Code:** Make sure you create two Python files (`data_extraction.py` and `authentication.py`) using the code provided in your Appendix [cite: 314, 354] and upload them.
3.  **Add a `requirements.txt`:** Create a file named `requirements.txt` containing:
    ```text
    pyserial
    numpy
    scipy
    ```
