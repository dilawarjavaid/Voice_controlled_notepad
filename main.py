import sys
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QTextEdit, QPushButton, QFileDialog
from PyQt6.QtCore import QThread, pyqtSignal

class SpeechRecognitionThread(QThread):
    result = pyqtSignal(str)
    error = pyqtSignal(str)
