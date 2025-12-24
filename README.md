# InstaHelp-AI

InstaHelp-AI is a fast, intent-based AI chatbot built using natural language processing techniques.
It is designed to answer questions related to computer science, programming, AI, Python, and core CS subjects with instant and reliable responses.

The chatbot prioritizes speed, correctness, and predictability, making it suitable for educational demos, beginner learning tools, and Streamlit deployment.

---

## What This Project Is

InstaHelp-AI is an intent-recognition chatbot that uses semantic sentence embeddings to understand user queries and map them to predefined knowledge areas.

Instead of generating answers dynamically, the chatbot:
- Understands the meaning of the user input
- Matches it against known intents
- Returns a confident, predefined response

This design avoids hallucinations and ensures consistent, correct answers.

---

## How It Works

- The user enters a query in natural language.
- The input is converted into a semantic embedding using a pretrained NLP model.
- The system compares the input embedding with stored intent embeddings.
- The most similar intent is selected using cosine similarity.
- The response associated with that intent is returned.

If no intent matches with sufficient confidence, a safe fallback response is shown.

---

## Tech Stack Used

- Python  
- Sentence Transformers (MiniLM)  
- Scikit-learn  
- NumPy  
- Streamlit  

---

## Model Used

- all-MiniLM-L6-v2 (Sentence Transformer)

This lightweight pretrained model is used only for semantic similarity matching, not for text generation.
It runs efficiently on CPU and enables instant responses.

---

## Project Structure

```
InstaHelp-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── chatbot/
    ├── __init__.py
    ├── intents.py
    └── model.py
```

---

## Installation and Setup

1. Clone the repository:

```bash
git clone <repository-link>
```

2. Navigate to the project directory:

```bash
cd InstaHelp-AI
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the environment:

a. Windows:
```bash
venv\Scripts\activate
```
b. Linux / macOS:
```bash
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

1. Start the Streamlit app using:

```bash
streamlit run app.py
```

2. Once launched, open your browser and go to:

```
http://localhost:8501
```

---

## Example Questions

1. What is CS?
2. What is computer science?
3. What is AI?
4. What is machine learning?
5. What is deep learning?
6. What is Python?
7. What is the basic syntax of Python?
8. What are Python basics?
9. What is DSA?
10. What is an operating system?
11. What is DBMS?
12. What is SQL?
13. What is web development?
14. Difference between frontend and backend
15. What are careers in computer science?

---

## Notes

- No external APIs are used.
- No datasets are required.
- All responses are deterministic and intent-driven.
- Designed for fast execution and Streamlit Cloud deployment.

---

## License

This project is intended for educational and learning purposes only.


By Jairaj R
