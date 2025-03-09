# 🧠 NLP Chatbot using Flask

This is a simple **NLP-based Chatbot** built using **Flask**, **NLTK**, and **TF-IDF Vectorization**. It can process user input, generate responses using **cosine similarity**, and maintain a session-based chat history.

## 🚀 Features
- 🔹 **Flask Web Interface** – User-friendly chatbot UI with session-based history.
- 🔹 **NLP Processing** – Uses **NLTK** for **tokenization and sentence similarity**.
- 🔹 **TF-IDF & Cosine Similarity** – Finds the most relevant response from stored text data.
- 🔹 **Session Management** – Maintains chat history using Flask sessions.
- 🔹 **Predefined Greeting Responses** – Recognizes basic greetings like "hello" or "hi".

## 🎬 Demo  
[🔗 Click here to see the chatbot in action](https://drive.google.com/file/d/1PH-GhQ8Hu3H7Awb6Kasy2XxYeikghLsk/view?usp=sharing)

## 🛠️ Tech Stack
- **Python** 🐍
- **Flask** 🌐
- **NLTK** 📝
- **scikit-learn** 📊
- **HTML & CSS** 🎨

## 🏗️ Installation & Setup

### 📌 Prerequisites
Ensure you have **Python 3.8+** installed along with `pip`.

### 📥 Clone the Repository
```bash
git clone https://github.com/your-username/nlp-chatbot-flask.git
cd nlp-chatbot-flask
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
python fpnlp.py
```

The chatbot will be accessible at:
```
http://127.0.0.1:5000/
```

## 🏗️ Project Structure
```
📂 nlp-chatbot-flask
 ┣ 📜 fpnlp.py             # Flask Application
 ┣ 📜 templates/
 ┃ ┗ 📜 index.html         # Chatbot UI
 ┣ 📜 static/
 ┃ ┗ 📜 styles.css         # Styles for Chat UI
 ┣ 📜 education.txt        # Dataset (used for chatbot responses)
 ┣ 📜 requirements.txt     # Python Dependencies
 ┗ 📜 README.md            # Project Documentation
```

## 📜 API Endpoints
| Endpoint     | Method | Description |
|-------------|--------|-------------|
| `/`         | `GET`  | Chat interface |
| `/`         | `POST` | Process user input & return response |
| `/clear_chat` | `GET`  | Clears chat history |

## 💡 How It Works
1. The chatbot loads text data from `education.txt` and preprocesses it.
2. **NLTK** tokenizes sentences, and **TF-IDF** is used for similarity scoring.
3. User input is **compared with stored sentences** using **cosine similarity**.
4. The **best matching response** is returned or a default fallback message.

## 🛠️ Customization
- 📝 **Modify the dataset**: Replace `education.txt` with your own text data.
- 🎨 **Change UI**: Modify `templates/index.html` and `static/styles.css`.
- 🤖 **Improve AI**: Implement **Transformer models (BERT/GPT-3)** for better responses.

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue if you find a bug or have an idea for improvement.

## 📄 License
This project is **open-source**.

---
🔹 **Developed by [Gandham Jayaditya]** 🔹  
📧 **Contact:** [jayadityagandham9@gmail.com]

