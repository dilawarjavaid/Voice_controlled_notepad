import sys
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QTextEdit, QPushButton, QFileDialog
from PyQt6.QtCore import QThread, pyqtSignal

class SpeechRecognitionThread(QThread):
    result = pyqtSignal(str)
    error = pyqtSignal(str)

    def run(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                self.result.emit("Listening... Speak now!")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                self.result.emit(text)
            except sr.UnknownValueError:
                self.error.emit("Sorry, could not understand the audio.")
            except sr.RequestError as e:
                self.error.emit(f"Could not request results, error: {e}")




# Main Application
class VoiceNotepad(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice-Controlled Notepad")
        self.setGeometry(300, 200, 600, 400)

        # Layouts
        self.layout = QVBoxLayout()

        # Text Editor
        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.text_edit)

        # Buttons
        self.listen_button = QPushButton("Start Listening")
        self.save_button = QPushButton("Save to File")
        self.layout.addWidget(self.listen_button)
        self.layout.addWidget(self.save_button)

        # Connect buttons
        self.listen_button.clicked.connect(self.start_listening)
        self.save_button.clicked.connect(self.save_to_file)

        self.setLayout(self.layout)

        # Speech Recognition Thread
        self.speech_thread = SpeechRecognitionThread()
        self.speech_thread.result.connect(self.add_text)
        self.speech_thread.error.connect(self.show_error)

