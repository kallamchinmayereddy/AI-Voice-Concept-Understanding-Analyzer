import os
from speech_to_text import SpeechToText
from semantic_similarity import SemanticSimilarity
from audio_features import AudioFeatureExtractor
from scoring_engine import ScoringEngine
from feedback_generator import FeedbackGenerator

import streamlit as st
import tempfile


from retriever import KnowledgeRetriever


@st.cache_resource
def load_models():

    speech_engine = SpeechToText()

    semantic_engine = SemanticSimilarity()

    audio_engine = AudioFeatureExtractor()

    score_engine = ScoringEngine()

    feedback_engine = FeedbackGenerator()
    retriever = KnowledgeRetriever()

    return (
        retriever,
        speech_engine,
        semantic_engine,
        audio_engine,
        score_engine,
        feedback_engine
    )

# -------------------------------------------------
# Streamlit Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Voice Concept Understanding Analyzer",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ Voice Concept Understanding Analyzer")
st.markdown("---")

# -------------------------------------------------
# Initialize Modules
# -------------------------------------------------

(
    retriever,
    speech_engine,
    semantic_engine,
    audio_engine,
    score_engine,
    feedback_engine
) = load_models()

# -------------------------------------------------
# Subject & Topic Selection
# -------------------------------------------------

subjects = retriever.get_subjects()





selected_subject = st.selectbox(
    "Select Subject",
    subjects
)

topics = retriever.get_topics(selected_subject)

selected_topic = st.selectbox(
    "Select Topic",
    topics
)

reference_answer = retriever.get_reference_answer(
    selected_subject,
    selected_topic
)

# -------------------------------------------------
# Display Reference Answer
# -------------------------------------------------

# st.subheader("Reference Answer")

# st.text_area(
#     "Knowledge Base Content",
#     reference_answer,
#     height=300
# )

# -------------------------------------------------
# Upload Audio
# -------------------------------------------------

audio_file = st.file_uploader(
    "Upload your audio",
    type=["wav", "mp3", "mpeg", "m4a"]
)

analyze = st.button("Analyze")

# =================================================
# Analysis Starts Here
# =================================================

if analyze:

    if audio_file is None:
        st.error("Please upload an audio file.")

    else:

        # -----------------------------------------
        # Save Uploaded Audio
        # -----------------------------------------

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mpeg"
        ) as temp_audio:

            temp_audio.write(audio_file.read())
            audio_path = temp_audio.name

        try:

            st.success("Audio uploaded successfully!")

            # -----------------------------------------
            # Speech to Text
            # -----------------------------------------

            with st.spinner("Transcribing audio..."):
                try:
                    student_answer = speech_engine.transcribe(audio_path)
                except Exception as e:
                    st.error("""
❌ Failed to transcribe the uploaded audio.

Possible reasons:
• Audio is unclear.
• No speech was detected.
• Unsupported audio encoding.

Please upload a clearer recording and try again.
""")
                    st.exception(e)
                    st.stop()

            st.subheader("Student Answer")
            st.write(student_answer)

            # -----------------------------------------
            # Semantic Similarity
            # -----------------------------------------

            try:
                score = semantic_engine.calculate_similarity(
                    reference_answer,
                    student_answer
                )
            except Exception as e:
                st.error("""
❌ Failed to compare your answer with the reference answer.

Please try again.
""")
                st.exception(e)
                st.stop()

            st.metric(
                "Semantic Similarity",
                f"{score * 100:.2f}%"
            )

            # -----------------------------------------
            # Audio Feature Extraction
            # -----------------------------------------

            with st.spinner("Analyzing speech features..."):
                try:
                    features = audio_engine.extract_features(
                        audio_path,
                        student_answer
                    )
                except Exception as e:
                    st.error("""
❌ Failed to analyze speech features.

Possible reasons:
• Poor audio quality.
• Unsupported audio format.
• Audio processing failed.

Please upload another recording.
""")
                    st.exception(e)
                    st.stop()

            # -----------------------------------------
            # Evaluation
            # -----------------------------------------

            try:
                evaluation = score_engine.evaluate(
                    score,
                    features
                )
            except Exception as e:
                st.error("""
❌ Failed to evaluate the results.

Please try again.
""")
                st.exception(e)
                st.stop()

            # -----------------------------------------
            # Feedback Generation
            # -----------------------------------------

            try:
                feedback = feedback_engine.generate_feedback(
                    evaluation
                )
            except Exception as e:
                st.error("""
❌ Failed to generate feedback.

Please try again.
""")
                st.exception(e)
                st.stop()

            # -----------------------------------------
            # Report
            # -----------------------------------------

            st.divider()
            st.header("📊 Evaluation Report")

            st.metric(
                "Overall Score",
                f"{evaluation.overall_score}%"
            )

            # -----------------------------------------
            # Individual Scores
            # -----------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Semantic Score",
                    f"{evaluation.semantic_score}%"
                )

            with col2:
                st.metric(
                    "Fluency Score",
                    f"{evaluation.fluency_score}%"
                )

            with col3:
                st.metric(
                    "Confidence Score",
                    f"{evaluation.confidence_score}%"
                )

            # -----------------------------------------
            # Speech Details
            # -----------------------------------------

            st.subheader("🎤 Speech Details")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Speech Duration",
                    f"{evaluation.duration:.2f} sec"
                )

            with col2:
                st.metric(
                    "Speaking Speed",
                    f"{evaluation.speech_rate:.2f} words/sec"
                )

            # -----------------------------------------
            # Strengths
            # -----------------------------------------

            st.subheader("✅ Strengths")

            for strength in feedback.strengths:
                st.success(strength)

            # -----------------------------------------
            # Areas for Improvement
            # -----------------------------------------

            st.subheader("⚠️ Areas for Improvement")

            for improvement in feedback.improvements:
                st.warning(improvement)

            # -----------------------------------------
            # Overall Assessment
            # -----------------------------------------

            st.subheader("📝 Overall Assessment")
            st.info(feedback.summary)

        except FileNotFoundError:

            st.error("""
❌ Audio file not found.

Please upload the audio again.
""")

        except RuntimeError as e:

            st.error("""
❌ A runtime error occurred while processing the audio.

Please try again with another recording.
""")
            st.exception(e)

        except Exception as e:

            st.error("""
❌ An unexpected error occurred.

Please make sure:
• The audio file is valid.
• The recording is clear.
• The file format is supported (.wav, .mp3, .mpeg, .m4a).

Then try again.
""")
            st.exception(e)

        finally:

            if os.path.exists(audio_path):
                os.remove(audio_path)