import sys
import os
import keyboard
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt, QTimer
from dotenv import load_dotenv

from ui.overlay_window import StealthOverlay
from ui.settings_window import SettingsWindow
from core.ai_handler import AIHandler
from core.audio_processor import AudioProcessor
from core.screen_analyzer import ScreenAnalyzer

load_dotenv()

class GhostWriter:
    def __init__(self):
        # Initialize components
        self.overlay = StealthOverlay()
        self.settings = SettingsWindow()
        self.ai_handler = AIHandler()
        self.audio_processor = AudioProcessor()
        self.screen_analyzer = ScreenAnalyzer()
        
        # Connect signals
        self.setup_connections()
        
        # Setup global hotkeys
        self.setup_hotkeys()
        
        # Show overlay
        self.overlay.show()
    
    def setup_connections(self):
        """Setup signal connections between components"""
        # Settings window connections
        self.overlay.settings_button.clicked.connect(self.settings.show)
        
        # Audio processor connections
        self.overlay.listen_button.clicked.connect(self.toggle_listening)
        self.audio_processor.transcription_ready.connect(self.handle_transcription)
        self.audio_processor.error_occurred.connect(self.handle_error)
        
        # Screen analyzer connections
        self.screen_analyzer.analysis_ready.connect(self.handle_screen_analysis)
        self.screen_analyzer.error_occurred.connect(self.handle_error)
        
        # Manual question handling
        self.overlay.question_submitted.connect(self.handle_manual_question)
    
    def setup_hotkeys(self):
        """Setup global hotkeys"""
        # Toggle listening: Ctrl+Alt+L
        keyboard.add_hotkey('ctrl+alt+l', self.toggle_listening)
        
        # Analyze screen: Ctrl+Alt+A
        keyboard.add_hotkey('ctrl+alt+a', self.analyze_screen)
        
        # Focus question input: Ctrl+Alt+Q
        keyboard.add_hotkey('ctrl+alt+q', self.focus_question_input)
        
        # Toggle overlay visibility: Ctrl+Alt+H
        keyboard.add_hotkey('ctrl+alt+h', self.toggle_overlay)
    
    def toggle_listening(self):
        """Toggle audio listening on/off"""
        if self.audio_processor.is_listening:
            self.audio_processor.stop_listening()
            self.overlay.listen_button.setText("🎤")
            self.overlay.append_response("Listening stopped.")
        else:
            self.audio_processor.start()
            self.overlay.listen_button.setText("⏹️")
            self.overlay.append_response("Listening started...")
    
    def handle_transcription(self, text: str):
        """Handle transcribed text from audio"""
        # Get context if available
        context = self.settings.get_master_context()
        
        # Generate AI response
        for response_chunk in self.ai_handler.generate_response(text, context):
            self.overlay.append_response(response_chunk)
    
    def analyze_screen(self):
        """Analyze current screen content"""
        self.screen_analyzer.start()
    
    def handle_screen_analysis(self, text: str):
        """Handle extracted text from screen"""
        # Get context if available
        context = self.settings.get_master_context()
        
        # Generate analysis
        analysis = self.ai_handler.analyze_screen(text, context)
        self.overlay.append_response("\n=== Screen Analysis ===\n" + analysis)
    
    def handle_manual_question(self, question: str):
        """Handle manually typed questions"""
        # Get context if available
        context = self.settings.get_master_context()
        
        # Generate AI response
        for response_chunk in self.ai_handler.generate_response(question, context):
            self.overlay.append_response(response_chunk)
    
    def handle_error(self, error_msg: str):
        """Handle errors from any component"""
        self.overlay.append_response(f"\nError: {error_msg}")
    
    def focus_question_input(self):
        """Focus the question input field"""
        self.overlay.input_field.setFocus()
    
    def toggle_overlay(self):
        """Toggle overlay visibility"""
        if self.overlay.isVisible():
            self.overlay.hide()
        else:
            self.overlay.show()

def main():
    # Create application
    app = QApplication(sys.argv)
    
    # Check Tesseract installation
    screen_analyzer = ScreenAnalyzer()
    if not screen_analyzer.check_tesseract_installation():
        print("Please install Tesseract-OCR to use screen analysis features.")
    
    # Create and initialize main application
    ghostwriter = GhostWriter()
    
    # Start application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 