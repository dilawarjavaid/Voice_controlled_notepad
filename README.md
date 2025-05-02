A simple PyQt6 desktop app that lets you **speak to take notes**, **view transcriptions**, and **save them to a file**.

## ⚙️ Features

* 🎤 Convert voice to text using your microphone
* 🖊️ Display transcribed text in a notepad-style editor
* 💾 Save notes as `.txt` files
* 🚀 Non-blocking UI with multithreaded speech recognition

## 🛠 Tech Stack

* **Python 3.7+**
* **PyQt6** – GUI framework
* **speech\_recognition** – For voice-to-text
* **Google Web Speech API** – Backend for recognition
* **QThread** – Keeps UI responsive

## ▶️ How to Run

1. **Install dependencies**:

   ```bash
   pip install PyQt6 SpeechRecognition PyAudio
   ```

   > *Note: On some systems, you may need to install `PyAudio` with system-specific commands.*

2. **Run the app**:

   ```bash
   python main.py
   ```

## 📝 Usage

* Click **"Start Listening"** and speak.
* Your speech appears as text in the editor.
* Click **"Save to File"** to export as `.txt`.

