#Before doing anything else, I need to import the ChatterBot which is done like this:
from chatterbot import ChatBot
from time import sleep
from chatterbot.trainers import ListTrainer


bot = ChatBot('Mike')#I start the ChatBot class, and create a Bot called “Mike”:
    
    
#ChatterBot has adapter classes that allow you to connect to different types of databases.
#In my code I decided to use the SQLStorageAdapter class, as it allows me to connect to SQL databases.
#By default, it creates an SQLite database in the “chatbot.py” directory.
bot = ChatBot(
'Mike',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
database_uri='sqlite:///database.sqlite3'
)
    
    
#I created a list of questions and answers that will be used as Mike's initial knowledge.
#In the code below I import the ListTrainer() method, it is responsible for allowing -> 
#my list of strings with questions and answers to be used as a basis for Mike's learning process
talk = ListTrainer(bot)
talk.train([
    "Hi there!", #User 
    "Hello", #Mike
    "How are you?", #User
    "I am good.", #Mike
    '"That is good to hear.", #User
    "Thank you",#Mike
])
sleep(0.5)

#I create an infinite loop with the while for Mike to receive the user's question, analyze, process and answer!
#in Mike's answer I use the confidence() function, to define that if the answer's confidence level is less than 0.5 ->
#he will inform you that he still does not know how to answer such a question.

#I used “Try” and “except” to be able to exit the loop and interrupt the program when a user types “ctrl + c”.
while True:
    try:
        answer = bot.get_response(input("User: "))
        if float(answer.confidence) > 0.5:
            print("Mike: ", answer)
        else:
            print("I don't understand :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
