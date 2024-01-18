# A dictionary that stores questions and answers
# Have a variable that trucks the score of the player
# loop through the dictionary using key values pairs
# Display each question to the user and allow them to answer
# Tell them if they are right or wrong
# Show the final results when the quiz is completed

quiz = {
    "question1":{
        "question":"What is the capital of Kenya?",
        "answer":"Nairobi"
    },
    "question2":{
        "question":"What is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"What is the capital of Italy?",
        "answer":"Rome"
    },
    "question4":{
        "question":"What is the capital of China?",
        "answer":"Beijing"
    },
    "question5":{
        "question":"What is the capital of Tanzania?",
        "answer":"Dondoma"
    },
    "question6":{
        "question":"What is the capital of Spain?",
        "answer":"Madrid"
    },
    "question7":{
        "question":"What is the capital of Brazil?",
        "answer":"Brasília"
    },
    "question8":{
        "question":"What is the capital of Argentina?",
        "answer":"Buenos Aires"
    },
    "question9":{
        "question":"What is the capital of USA?",
        "answer":"Washington DC"
    },
    "question10":{
        "question":"What is the capital of England?",
        "answer":"London"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("Correct \n")
        score = score + 1
    else:
        print("Wrong!")
        print("The answer is: "+ value['answer']+"\n")

if score == 10:
    print("Genious👏👏👏👏👏\n")
    print("Final Score: "+ str(score*10) +"%")   
elif score >= 7:
    print("Exellent👏👏👏\n")
    print("Final Score: "+ str(score*10) +"%")
else:
    print("Final Score: "+ str(score*10)+"%")