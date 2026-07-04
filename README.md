# AI-Voice-Concept-Understanding-Analyzer
# 🎙️ Voice Concept Understanding Analyzer

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B)](https://streamlit.io/)
[![Whisper](https://img.shields.io/badge/Whisper-Speech%20to%20Text-4B8BBE)](https://github.com/openai/whisper)
[![Sentence Transformers](https://img.shields.io/badge/Sentence%20Transformers-Semantic%20Similarity-6A5ACD)](https://www.sbert.net/)

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Workflow](#system-workflow)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---



## 🌟 Project Overview

Voice Concept Understanding Analyzer is an AI-powered educational assessment system that evaluates a student's conceptual understanding from spoken explanations using speech recognition, semantic similarity, and speech feature analysis.

Unlike traditional systems that rely on keyword matching, this application assesses how well a student understands a concept by comparing the meaning of their explanation with expert reference material and providing detailed feedback.

The application guides the user through a simple workflow:

1. Selects a subject.
2. Selects a topic.
3. Uploads an audio explanation.
4. The system transcribes the speech.
5. Compares the spoken explanation with a reference answer stored in the local knowledge base.
6. Evaluates conceptual similarity.
7. Analyzes speech characteristics.
8. Generates an overall score and detailed feedback.

This makes it a strong portfolio project for demonstrating speech processing, semantic analysis, and educational AI in a practical application.

---

## ✨ Features

- Speech-to-text transcription using Whisper
- Semantic similarity scoring using Sentence Transformers (Sentence-BERT)
- Subject and topic selection from a built-in knowledge base
- Local knowledge base retrieval for reference answers
- Speech feature extraction such as duration, estimated speaking rate, and audio energy
- AI-based evaluation scoring and report generation
- Strengths and improvement suggestions for learner feedback
- Streamlit-based interactive web interface
- Modular architecture with separate components for transcription, retrieval, scoring, and feedback

---

## 🛠️ Tech Stack

| Category | Technology | Version |
| --- | --- | --- |
| Programming Language | Python | 3.10+ |
| Web App Framework | Streamlit | 1.58.0 |
| Speech-to-Text | OpenAI Whisper | 20250625 |
| Semantic Similarity | Sentence Transformers | 5.6.0 |
| Deep Learning Backend | PyTorch | 2.11.0 |
| Audio Processing | Librosa | 0.11.0 |
| Machine Learning | Scikit-learn | 1.7.2 |
| Numerical Computing | NumPy | 1.26.4 |
| Scientific Computing | SciPy | 1.15.3 |
| Audio I/O | SoundFile | 0.14.0 |

---

## 🔄 System Workflow

```mermaid
flowchart LR

A[Select Subject & Topic]
-->B[Retrieve Reference Answer]

B-->C[Upload Audio]

C-->D[Whisper Speech-to-Text]

D-->E[Sentence-BERT Similarity]

E-->F[Speech Feature Extraction]

F-->G[Scoring Engine]

G-->H[Feedback Generator]

H-->I[Evaluation Report]
```

---

## 📁 Project Structure

```text
SIP Project/
├── audio_features.py
├── config.py
├── evaluation_report.py
├── feedback_generator.py
├── feedback_report.py
├── knowledge_generator.py
├── knowledge_base/
│   ├── Artificial Intelligence/
│   │   ├── Deep Learning.txt
│   │   ├── Expert Systems.txt
│   │   ├── Introduction.txt
│   │   ├── Knowledge Representation.txt
│   │   └── Machine Learning.txt
│   ├── Data Structures/
│   │   ├── Arrays.txt
│   │   ├── Hash Tables.txt
│   │   └── Stacks.txt
│   └── Machine Learning/
│       ├── Classification.txt
│       ├── Decision Trees.txt
│       ├── Introduction.txt
│       ├── Model Evaluation.txt
│       ├── Neural Networks.txt
│       ├── Overfitting.txt
│       ├── Random Forest.txt
│       ├── Regression.txt
│       ├── Reinforcement Learning.txt
│       ├── Supervised Learning.txt
│       └── Unsupervised Learning.txt
├── prompts.py
├── requirements.txt
├── retriever.py
├── sample_audio/
│   └── sample_sip_1.mpeg
├── scoring_engine.py
├── semantic_similarity.py
├── settings.py
├── speech_to_text.py
├── streamlit_app.py
└── topics.py
```

---

## ⚙️ Installation

Clone the repository and install the dependencies:

```bash
git clone <your-repository-url>
cd "SIP Project"
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

---

## 🚀 Usage

1. Launch the application using Streamlit.
2. Select a subject from the available options.
3. Choose a topic under that subject.
4. Upload an audio file containing your spoken explanation.
5. Click the Analyze button.
6. Review the transcription, similarity score, speech analysis, and feedback report.

---

## 📊 Sample Output

The evaluation report includes:

- Overall Score
- Semantic Score
- Fluency Score
- Confidence Score
- Speech Details such as duration and speaking speed
- Strengths identified from the explanation
- Areas for Improvement
- An overall assessment summary

---

## 🔮 Future Enhancements

Possible improvements for the project include:

- Retrieval-Augmented Generation (RAG) for richer context retrieval
- Dynamic knowledge base generation using large language models
- Question-answer mode for interactive learning
- User authentication and saved history
- Performance analytics dashboard for learners and educators
- Adaptive scoring using LLMs
- Multi-language support
- Personalized learning recommendations

---

## 👤 Author

This project is suitable for showcasing AI, NLP, speech processing, and full-stack-style application development skills in a portfolio.

- Name: Kallam Chinmaye Naga Purnima
- GitHub: [Github](https://github.com/kallamchinmayereddy)
- Email: kchinmayereddy@gmail.com

---

## ✅ Summary

The Voice Concept Understanding Analyzer combines speech recognition, semantic similarity, and educational feedback into one practical application. It is a strong example of how AI can be used to assess conceptual understanding in a more meaningful way than simple keyword matching.
