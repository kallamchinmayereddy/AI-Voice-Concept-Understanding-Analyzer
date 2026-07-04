import os

from settings import KNOWLEDGE_BASE_PATH


class KnowledgeRetriever:

    def __init__(self):
        self.base_path = KNOWLEDGE_BASE_PATH

    def get_subjects(self):

        subjects = []

        for item in os.listdir(self.base_path):

            path = os.path.join(self.base_path, item)

            if os.path.isdir(path):
                subjects.append(item)

        subjects.sort()

        return subjects
    def get_topics(self, subject):

        folder_path = os.path.join(
            self.base_path,
            subject
        )

        topics = []

        for file in os.listdir(folder_path):

            if file.endswith(".txt"):

                topic = file.replace(".txt", "")

                topics.append(topic)

        topics.sort()

        return topics    
    def get_reference_answer(self, subject, topic):

        file_path = os.path.join(
            self.base_path,
            subject,
            f"{topic}.txt"
        )

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"{topic}.txt not found in {subject}"
            )

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()