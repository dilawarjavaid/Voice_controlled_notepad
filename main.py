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

