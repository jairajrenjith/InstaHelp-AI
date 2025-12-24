INTENTS = {

    # ======================================================
    # GENERAL CONVERSATION
    # ======================================================

    "greeting": {
        "examples": [
            "hi", "hello", "hey", "hey there",
            "good morning", "good afternoon", "good evening"
        ],
        "response": "Hello 👋 How can I help you today?"
    },

    "status": {
        "examples": [
            "how are you", "how are you doing",
            "are you okay", "how's it going", "what's up"
        ],
        "response": "I’m doing great 😊 Thanks for asking!"
    },

    "about_bot": {
        "examples": [
            "who are you", "what are you",
            "what is this bot", "what can you do",
            "your purpose"
        ],
        "response": "I’m InstaHelp, a fast AI chatbot that answers questions related to computer science and technology."
    },

    # ======================================================
    # CS / COMPUTER SCIENCE (ABBREVIATION SAFE)
    # ======================================================

    "cs_definition": {
        "examples": [
            "cs", "what is cs", "cs meaning",
            "cs full form", "computer science",
            "what is computer science",
            "define computer science",
            "computer science meaning",
            "about cs",
            "cs subject"
        ],
        "response": "CS stands for Computer Science. It is the study of computers, programming, algorithms, data, and software systems."
    },

    "cs_topics": {
        "examples": [
            "cs topics", "computer science topics",
            "subjects in cs", "core cs subjects",
            "what are cs subjects",
            "computer science syllabus"
        ],
        "response": "Core CS subjects include Programming, DSA, DBMS, Operating Systems, Computer Networks, and Software Engineering."
    },

    "cs_careers": {
        "examples": [
            "cs careers", "jobs in cs",
            "computer science jobs",
            "career in computer science",
            "cs job roles"
        ],
        "response": "Careers in CS include Software Developer, Data Scientist, ML Engineer, Web Developer, and System Engineer."
    },

    # ======================================================
    # AI / ML / DL (FULL ABBREVIATION HANDLING)
    # ======================================================

    "ai_definition": {
        "examples": [
            "ai", "what is ai", "ai meaning",
            "ai full form", "artificial intelligence",
            "define ai", "about ai"
        ],
        "response": "AI stands for Artificial Intelligence. It focuses on creating machines that can perform tasks requiring human intelligence."
    },

    "ai_applications": {
        "examples": [
            "ai applications", "uses of ai",
            "where is ai used", "ai in real life",
            "applications of artificial intelligence"
        ],
        "response": "AI is used in healthcare, finance, recommendation systems, autonomous vehicles, fraud detection, and chatbots."
    },

    "ml_definition": {
        "examples": [
            "ml", "what is ml", "ml meaning",
            "machine learning", "define machine learning",
            "about ml"
        ],
        "response": "ML stands for Machine Learning. It is a subset of AI that enables systems to learn patterns from data."
    },

    "types_of_ml": {
        "examples": [
            "types of ml",
            "supervised learning",
            "unsupervised learning",
            "reinforcement learning"
        ],
        "response": "Machine Learning types include supervised, unsupervised, and reinforcement learning."
    },

    "dl_definition": {
        "examples": [
            "dl", "what is dl", "deep learning",
            "define deep learning", "dl meaning"
        ],
        "response": "Deep Learning is a subset of ML that uses multi-layer neural networks to learn complex patterns."
    },

    # ======================================================
    # PYTHON (DETAILED)
    # ======================================================

    "python_definition": {
        "examples": [
            "python", "what is python",
            "python meaning", "python language",
            "about python programming"
        ],
        "response": "Python is a high-level, easy-to-learn programming language used in web development, AI, automation, and data science."
    },

    "python_features": {
        "examples": [
            "features of python",
            "advantages of python",
            "why python is popular"
        ],
        "response": "Python is popular due to its readability, simplicity, large libraries, and strong community support."
    },

    "python_syntax": {
        "examples": [
            "python syntax",
            "basic syntax of python",
            "python indentation",
            "how python syntax works"
        ],
        "response": "Python uses indentation instead of braces to define code blocks, making programs clean and readable."
    },

    "python_basics": {
        "examples": [
            "python basics",
            "fundamentals of python",
            "python for beginners",
            "how to start python"
        ],
        "response": "Python basics include variables, data types, conditionals, loops, and functions."
    },

    "python_oops": {
        "examples": [
            "oops in python",
            "object oriented programming in python",
            "classes and objects in python"
        ],
        "response": "Python supports OOP concepts such as classes, objects, inheritance, encapsulation, and polymorphism."
    },

    # ======================================================
    # DSA / ALGORITHMS
    # ======================================================

    "dsa_definition": {
        "examples": [
            "dsa", "what is dsa",
            "data structures and algorithms",
            "define dsa"
        ],
        "response": "DSA stands for Data Structures and Algorithms. It focuses on organizing data efficiently and solving problems optimally."
    },

    "data_structures": {
        "examples": [
            "data structures",
            "types of data structures",
            "list stack queue tree graph"
        ],
        "response": "Common data structures include arrays, linked lists, stacks, queues, trees, and graphs."
    },

    "algorithms": {
        "examples": [
            "what is algorithm",
            "define algorithm",
            "types of algorithms"
        ],
        "response": "An algorithm is a step-by-step procedure used to solve a problem efficiently."
    },

    # ======================================================
    # OPERATING SYSTEM (OS)
    # ======================================================

    "os_definition": {
        "examples": [
            "os", "what is os", "operating system",
            "define os", "os meaning"
        ],
        "response": "An Operating System manages hardware resources and provides services to applications."
    },

    "os_functions": {
        "examples": [
            "functions of os",
            "what does an operating system do"
        ],
        "response": "An OS handles process management, memory management, file systems, and device control."
    },

    # ======================================================
    # DBMS / DATABASES
    # ======================================================

    "dbms_definition": {
        "examples": [
            "dbms", "what is dbms",
            "database management system",
            "define dbms"
        ],
        "response": "DBMS is software used to store, retrieve, and manage data efficiently in databases."
    },

    "sql_definition": {
        "examples": [
            "sql", "what is sql",
            "structured query language"
        ],
        "response": "SQL is a language used to query and manage data in relational databases."
    },

    # ======================================================
    # COMPUTER NETWORKS
    # ======================================================

    "computer_networks": {
        "examples": [
            "computer networks",
            "what is computer network",
            "lan wan man",
            "types of networks"
        ],
        "response": "Computer networks connect devices to share data, such as LAN, WAN, and MAN."
    },

    # ======================================================
    # WEB DEVELOPMENT
    # ======================================================

    "web_development": {
        "examples": [
            "web development",
            "what is web development",
            "web development basics"
        ],
        "response": "Web development involves building websites using frontend and backend technologies."
    },

    "frontend_backend": {
        "examples": [
            "frontend vs backend",
            "difference between frontend and backend"
        ],
        "response": "Frontend handles user interfaces, while backend manages servers, databases, and application logic."
    },

    "html_css_js": {
        "examples": [
            "html css js",
            "html css javascript",
            "web technologies"
        ],
        "response": "HTML structures content, CSS styles it, and JavaScript adds interactivity to websites."
    },

    # ======================================================
    # CAREER & LEARNING
    # ======================================================

    "learning_programming": {
        "examples": [
            "how to learn programming",
            "programming tips for beginners",
            "how to become good at coding"
        ],
        "response": "Practice consistently, understand fundamentals, build projects, and learn by doing."
    },

    "tech_careers": {
        "examples": [
            "careers in tech",
            "software jobs",
            "it career options"
        ],
        "response": "Tech careers include Software Engineer, Data Scientist, Cloud Engineer, and Cybersecurity Analyst."
    },

    # ======================================================
    # GOODBYE
    # ======================================================

    "goodbye": {
        "examples": [
            "bye", "goodbye", "see you",
            "exit", "quit"
        ],
        "response": "Goodbye 👋 Feel free to come back anytime!"
    }
}
