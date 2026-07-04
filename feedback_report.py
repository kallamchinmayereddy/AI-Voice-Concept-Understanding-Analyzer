from dataclasses import dataclass

@dataclass
class FeedbackReport:

    concept_understanding: str
    fluency: str
    confidence: str

    strengths: list[str]
    improvements: list[str]

    summary: str