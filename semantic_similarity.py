from sentence_transformers import SentenceTransformer
from sentence_transformers import util


class SemanticSimilarity:

    def __init__(self):
        print("Loading Sentence-BERT model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        print("Sentence-BERT model loaded successfully!")

    def calculate_similarity(self, reference_text, student_text):

        embedding1 = self.model.encode(reference_text, convert_to_tensor=True)

        embedding2 = self.model.encode(student_text, convert_to_tensor=True)

        similarity = util.cos_sim(embedding1, embedding2)

        return float(similarity[0][0])