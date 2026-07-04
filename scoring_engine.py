from evaluation_report import EvaluationReport


class ScoringEngine:

    def evaluate(self, semantic_score, features):

        # ----------------------------
        # Extract Features
        # ----------------------------
        speech_rate = features["Estimated Words Per Second"]
        rms_energy = features["Average RMS Energy"]
        duration = features["Duration (seconds)"]
        zero_crossing_rate = features["Average Zero Crossing Rate"]

        # ----------------------------
        # Semantic Score (70%)
        # ----------------------------
        semantic_marks = semantic_score * 70

        # ----------------------------
        # Fluency Score (15%)
        # ----------------------------
        if 2 <= speech_rate <= 3:
            fluency_marks = 15
        elif 1.5 <= speech_rate < 2:
            fluency_marks = 10
        else:
            fluency_marks = 5

        # ----------------------------
        # Confidence Score (10%)
        # ----------------------------
        if rms_energy >= 0.08:
            confidence_marks = 10
        else:
            confidence_marks = 5

        # ----------------------------
        # Duration Score (5%)
        # ----------------------------
        if duration >= 8:
            duration_marks = 5
        else:
            duration_marks = 2

        # ----------------------------
        # Overall Score
        # ----------------------------
        overall_score = round(
            semantic_marks
            + fluency_marks
            + confidence_marks
            + duration_marks,
            2
        )

        return EvaluationReport(
            overall_score=overall_score,
            semantic_score=round(semantic_score * 100, 2),
            fluency_score=round((fluency_marks / 15) * 100, 2),
            confidence_score=round((confidence_marks / 10) * 100, 2),
            duration_score=round((duration_marks / 5) * 100, 2),
            duration=duration,
            speech_rate=speech_rate,
            rms_energy=rms_energy,
            zero_crossing_rate=zero_crossing_rate
        )