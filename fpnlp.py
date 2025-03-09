from flask import Flask, render_template, request, session
import string
import random
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session to work

# Load the text data for responses
def load_text(file_path):
    with open(file_path, 'r') as file:
        text_data = file.read().lower()
    return text_data

def tokenize_and_clean(text):
    # Tokenize into sentences and words, removing punctuation
    sentences = sent_tokenize(text)
    return sentences

def greet_response(user_input):
    # Simple greeting logic
    greetings = ["hello", "hi", "greetings", "hey"]
    responses = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
    
    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(responses)
    return None

# Generate response using cosine similarity
def generate_response(user_input, sentences):
    # Add user input to sentences for similarity comparison
    sentences.append(user_input)
    
    # Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")  # Use built-in English stop words
    tfidf = vectorizer.fit_transform(sentences)
    similarity = cosine_similarity(tfidf[-1], tfidf)
    
    # Remove user input from sentences after processing
    sentences.pop()
    
    # Find best matching sentence based on cosine similarity
    response_idx = similarity.argsort()[0][-2]
    best_score = similarity[0][response_idx]
    
    # Define a response threshold
    if best_score > 0.2:
        return sentences[response_idx]
    else:
        return "I'm sorry, I didn't understand that."

def chatbot(user_input, sentences):
    user_input = user_input.lower()
    if greet_response(user_input):
        return greet_response(user_input)
    else:
        return generate_response(user_input, sentences)

# Initialize text data and chatbot
text_data = load_text("education.txt")  # Ensure the file path is correct
sentences = tokenize_and_clean(text_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize chat history if it's not already in the session
    if 'chat_history' not in session:
        session['chat_history'] = [{"type": "bot", "content": "Get started or ask something!"}]
        
    # Ensure sentences are initialized
    if 'sentences' not in session:
        session['sentences'] = sentences

    if request.method == 'POST':
        user_input = request.form['user_input']
        response = chatbot(user_input, session['sentences'])
        
        # Add user input and bot response to chat history
        session['chat_history'].append({"type": "user", "content": user_input})
        session['chat_history'].append({"type": "bot", "content": response})
        
        session.modified = True  # Mark session as modified

    return render_template('index.html', chat_history=session['chat_history'])

@app.route('/clear_chat')
def clear_chat():
    # Clear chat history and reinitialize the session for a fresh start
    session.pop('chat_history', None)
    session['chat_history'] = [{"type": "bot", "content": "Chat history cleared. Start a new conversation!"}]
    
    # Re-initialize the sentences from the loaded text
    session['sentences'] = tokenize_and_clean(load_text("education.txt"))
    
    # Return the new chat history and sentences to the template
    return render_template('index.html', chat_history=session['chat_history'])

if __name__ == '__main__':
    app.run(debug=True)
