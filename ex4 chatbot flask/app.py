from flask import Flask, render_template, request, send_file
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hey|hello",
    ["Hello", "Hey there", "Hi"]],
    [r"how are you ?",
    ["I'm doing good\nHow about You ?", "I am good, thank you"]],
    [r"i am fine",
    ["Great to hear that, How can I help you?", "How can I help you?"]],    
    [r"what is your name ?",
    ["I am a chatbot. You can ask me anything."]],
    [r"what courses do you offer ?",
    ["We offer various engineering courses including:\n- Computer Science\n- Mechanical\n- Civil\n- Electronics"]],
    [r"located",
    ["K.Ramakrishnan College of Engineering is located in Trichy, Tamil Nadu."]],
    [r"admission|apply",
    ["For admission details, please visit our website or contact our admission office at admissions@krce.ac.in"]],
    [r"bye|goodbye",
    ["Goodbye! Have a great day!", "See you later!"]],
    [r".*",
    ["I'm not sure I understand. Could you rephrase that?", "Could you please be more specific?"]],
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/get")
def get_bot_response():
        userText = request.args.get('msg')
        chat = Chat(pairs, reflections)
        return chat.respond(userText)

@app.route("/test")
def test():
    return "hello"
    
@app.route("/test1")
def test1():
    return send_file("templates/index.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)