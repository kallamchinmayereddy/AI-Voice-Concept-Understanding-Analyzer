import os
import time

from google import genai

from topics import SUBJECTS
from settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    KNOWLEDGE_BASE_PATH
)
from prompts import KNOWLEDGE_BASE_PROMPT


class KnowledgeBaseGenerator:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_topic(self, subject, topic):

        prompt = KNOWLEDGE_BASE_PROMPT.format(
            subject=subject,
            topic=topic
        )

        response = self.client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        if not response.text:
            raise Exception("Gemini returned an empty response.")

        return response.text.strip()

    def save_topic(self, subject, topic, content):

        folder_path = os.path.join(
            KNOWLEDGE_BASE_PATH,
            subject
        )

        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(
            folder_path,
            f"{topic}.txt"
        )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"      Saved: {file_path}")

    def topic_exists(self, subject, topic):

        file_path = os.path.join(
            KNOWLEDGE_BASE_PATH,
            subject,
            f"{topic}.txt"
        )

        return os.path.exists(file_path)        

    def generate_knowledge_base(self):

        for subject, topics in SUBJECTS.items():

            print(f"\nGenerating Subject: {subject}")

            for topic in topics:

                print(f"   Generating Topic: {topic}")
                if self.topic_exists(subject, topic):
                    print("      Already Exists ✓")
                    continue

                try:

                    content = self.generate_topic(
                        subject,
                        topic
                    )

                    self.save_topic(
                        subject,
                        topic,
                        content
                    )
                    time.sleep(2)  # Be respectful to the API

                    print("      Done")

                except Exception as e:

                    print(f"      Failed : {e}")
        # subject = "Machine Learning"
        # topic = "Introduction"

        # print(f"\nGenerating Subject: {subject}")
        # print(f"Generating Topic: {topic}")

        # content = self.generate_topic(subject, topic)

        # self.save_topic(
        #     subject,
        #     topic,
        #     content
        # )

        # print("Done!")

if __name__ == "__main__":

    generator = KnowledgeBaseGenerator()

    generator.generate_knowledge_base()