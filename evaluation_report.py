from dataclasses import dataclass

@dataclass
class EvaluationReport:
    overall_score: float
    semantic_score: float

    fluency_score: float
    confidence_score: float
    duration_score: float

    duration: float
    speech_rate: float
    rms_energy: float
    zero_crossing_rate: float