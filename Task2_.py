import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?"]],
    [r"what is cybersecurity?", ["Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks."]],
    [r"what is phishing?", ["Phishing is a type of cyberattack where attackers trick users into revealing sensitive information."]],
    [r"bye|goodbye", ["Goodbye! Stay safe online."]]
]

def chatbot():
    print("CyberBot: Hello! Ask me anything about cybersecurity. (Type 'bye' to exit)")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
