# Ghostwriter - AI Meeting Assistant

Ghostwriter is a high-performance, undetectable AI meeting assistant designed for online interviews and meetings. It provides real-time, AI-powered assistance while remaining completely invisible during screen sharing.

## Features

- **Stealth Overlay**: A completely undetectable, click-through window that stays on top of other applications
- **Real-time Audio Transcription**: Captures and transcribes system audio for instant AI analysis
- **Screen Analysis**: Extract and analyze text from any visible window
- **Context-Aware Responses**: Personalized answers based on your resume and job context
- **Local Processing**: Uses efficient local models where possible to minimize costs
- **Global Hotkeys**: Quick access to all features without visible interaction

## Requirements

- Windows 10/11
- Python 3.9+
- [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- Virtual Audio Cable (recommended for system audio capture)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ghostwriter.git
cd ghostwriter
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Tesseract-OCR:
   - Download the installer from [UB-Mannheim's repository](https://github.com/UB-Mannheim/tesseract/wiki)
   - Run the installer and note down the installation path

5. Create a `.env` file:
   - Copy `.env_example` to `.env`
   - Add your Google API key
   - Update the Tesseract path
   - Configure audio device settings

## Configuration

The `.env` file contains all necessary configuration:

```env
# Google Gemini API Key
GOOGLE_API_KEY=your_api_key_here

# Audio Settings
AUDIO_DEVICE_INDEX=1  # Set to your system's output mix device index
WHISPER_MODEL=base.en  # Options: tiny.en, base.en, small.en, medium.en

# OCR Settings
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

# UI Settings
OVERLAY_OPACITY=0.85
OVERLAY_COLOR=#2C2C2C
```

## Usage

1. Start the application:
```bash
python main.py
```

2. Configure your context:
   - Click the settings icon (⚙️) or press Ctrl+Alt+H to show the overlay
   - Enter your resume and job description
   - Click "Save Context"

3. Use the features:
   - **Toggle Listening**: Click 🎤 or press Ctrl+Alt+L
   - **Screen Analysis**: Press Ctrl+Alt+A
   - **Direct Questions**: Press Ctrl+Alt+Q
   - **Toggle Overlay**: Press Ctrl+Alt+H

## Audio Setup

For optimal audio capture:

1. Install a Virtual Audio Cable (VAC) software
2. Set the VAC as your default output device
3. Update the AUDIO_DEVICE_INDEX in .env to match your VAC's input device

## Security Notes

- API keys and personal information are stored locally
- All processing is done on your machine when possible
- The overlay window is completely invisible to screen sharing
- No data is sent to external servers except for AI API calls

## Troubleshooting

1. **No Audio Capture**:
   - Check your audio device index in .env
   - Verify your virtual audio cable setup
   - Try running as administrator

2. **OCR Not Working**:
   - Verify Tesseract installation
   - Check TESSERACT_PATH in .env
   - Ensure the path includes tesseract.exe

3. **Overlay Not Invisible**:
   - Restart the application
   - Try running as administrator
   - Check if your screen sharing software has special capture modes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 