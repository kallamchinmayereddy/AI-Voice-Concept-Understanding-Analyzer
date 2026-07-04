from feedback_report import FeedbackReport


class FeedbackGenerator:

    def generate_feedback(self, report):

        strengths = []
        improvements = []

        # ----------------------------
        # Concept Understanding
        # ----------------------------
        if report.semantic_score >= 85:
            concept_understanding = "Excellent"
            strengths.append(
                "You demonstrated a strong understanding of the concept."
            )

        elif report.semantic_score >= 70:
            concept_understanding = "Good"
            strengths.append(
                "You explained the concept reasonably well."
            )
            improvements.append(
                "Include a few more important details."
            )

        else:
            concept_understanding = "Needs Improvement"
            improvements.append(
                "Focus on explaining the core concept more accurately."
            )

        # ----------------------------
        # Fluency
        # ----------------------------
        if report.fluency_score >= 90:
            fluency = "Excellent"
            strengths.append(
                "Your speaking pace was excellent."
            )

        elif report.fluency_score >= 70:
            fluency = "Good"
            strengths.append(
                "Your speaking pace was good."
            )

        else:
            fluency = "Needs Improvement"
            improvements.append(
                "Try speaking a little faster and maintain a steady pace."
            )

        # ----------------------------
        # Confidence
        # ----------------------------
        if report.confidence_score >= 90:
            confidence = "Good"
            strengths.append(
                "You spoke with good confidence."
            )

        else:
            confidence = "Needs Improvement"
            improvements.append(
                "Speak a little louder and more confidently."
            )

        # ----------------------------
        # Duration
        # ----------------------------
        if report.duration < 8:
            improvements.append(
                "Spend a little more time explaining the concept."
            )

        # ----------------------------
        # Overall Summary
        # ----------------------------
        if report.overall_score >= 90:
            summary = "Excellent explanation with strong conceptual understanding."

        elif report.overall_score >= 75:
            summary = "Good explanation with minor areas for improvement."

        elif report.overall_score >= 60:
            summary = "Average explanation. More practice is recommended."

        else:
            summary = "The explanation needs significant improvement."

        return FeedbackReport(
            concept_understanding=concept_understanding,
            fluency=fluency,
            confidence=confidence,
            strengths=strengths,
            improvements=improvements,
            summary=summary
        )