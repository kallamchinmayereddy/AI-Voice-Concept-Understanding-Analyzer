import librosa
import numpy as np


class AudioFeatureExtractor:

    def extract_features(self, audio_path, transcript):

        # Load audio
        y, sr = librosa.load(audio_path, sr=None)

        # Duration
        duration = librosa.get_duration(y=y, sr=sr)

        # RMS Energy
        rms = librosa.feature.rms(y=y)
        avg_rms = float(np.mean(rms))

        # Zero Crossing Rate
        zcr = librosa.feature.zero_crossing_rate(y)
        avg_zcr = float(np.mean(zcr))

        # Estimated Speech Rate
        number_of_words = len(transcript.split())

        words_per_second = number_of_words / duration

        return {
            "Duration (seconds)": round(duration, 2),
            "Average RMS Energy": round(avg_rms, 4),
            "Average Zero Crossing Rate": round(avg_zcr, 4),
            "Estimated Words Per Second": round(words_per_second, 3)
        }