from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from chatbot.intents import INTENTS

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = []
responses = []

for intent in INTENTS.values():
    for example in intent["examples"]:
        sentences.append(example)
        responses.append(intent["response"])

sentence_embeddings = model.encode(sentences)

def get_response(user_input: str) -> str:
    user_embedding = model.encode([user_input])
    similarities = cosine_similarity(user_embedding, sentence_embeddings)[0]
    best_idx = np.argmax(similarities)

    if similarities[best_idx] > 0.55:
        return responses[best_idx]

    return "🤔 I’m not sure about that. Try asking about AI, Python, programming, or CS topics."
