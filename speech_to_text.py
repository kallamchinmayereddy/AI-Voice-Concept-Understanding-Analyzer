import whisper


class SpeechToText:

    def __init__(self):
        print("Loading Whisper model...")
        self.model = whisper.load_model("tiny")
        print("Whisper model loaded successfully!")

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result["text"]