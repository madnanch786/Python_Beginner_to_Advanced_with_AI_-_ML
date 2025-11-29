print("AOA! Welcome to Your ChatBot")
print("You can ask me basic question, type 'bye' to exit fro the bot")

# Chatbot Memory Creation [Dictionary of responses]
responses={
    "hello":"Hi, welcome. How can I help you?",
    "how are you":"I am very fine. Thank You!",
    "who are you":"I am smart AI chatbot",
    "motivate me":"Keep going. Every bug of your project makes you a better developer",
    "happy":"Great! to here that",
    "functions kya hotay hai":"jakar  chapter 7 parho"
}
# Methods/Functions to get response of ChatBot
def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I can't Answer this. I can do soon"    

# Take User Input
while True:
    userInput=input("Please ask your question:")
    reply=getResponseOfBot(userInput)
    print("Bot Response: ", reply)
    
    if "bye" in userInput.lower():
        break