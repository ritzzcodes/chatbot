pip install nltk
import nltk
from nltk.chat.util import Chat,reflections
reflections= {
    "i am" : "you are",
    "i was":"you were",
    "I":"you",
    "I'm": "you are",
    "my":"your",
    "you are":"I am",
    "you were": "I was",
    "you wil": "i will",
    "yours":"mine",
    "you":"me",
    "me":"you"
}

pairs=[
       [
        r"my name is (.*)",
        ["hello %1, How are you today?",]
       ],
       [
        r"hi",
        ["hello",]
        ],
       [
        r"what is your name?",
        ['i am a bot create by Ritwika, you can call me Veronica',]
        ],
       [
        r"how are you?",
        ["i am doing good",]
       ],
       [
        r'sorry(.*)',
        ["its okay",]
       ],
       [
        r"i'm (.*) doing good",
        ["nice to hear that",]
       ],
       [
        r"who (,*) sportsperson ?",
        ["messi","ronaldo","Virat"]
       ],
       [
        
        r'who (,*) actor?',
        ["Bradd Pitt"]
       ],
       [
        r"I am looking for some online guides",
        ["crazy tech has many articles related to this"]
       ],
       [
        r"quit",
        ["bye take care"]
       ],
       ]
 def chat():
   print("hi! i am a chatbot at your service now")
   chat=Chat(pairs,reflections)
    chat.converse()
if __name__=="__main___":
  chat()
