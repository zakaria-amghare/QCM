import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
import json
with open("questions.json","r") as file:
    globaldata=json.load(file)

def new_game(category):
    clear_terminal()
    scor=0
    question_number=1
    localdata=globaldata[category]
    for question in localdata:
        clear_terminal()
        print(f"{question_number}"+") "+question["question"])
        for option in question["options"]:
            print(option)
        guess=input("choose:")
        guess=guess.upper()
        clear_terminal()
        result=check_answer(question["answer"], guess)
        if result==1:
            scor=scor+result
        elif result== -1:
            break
        question_number=question_number+1
    print("you have:"+f"{scor}"+"piont")
    return scor
    

def check_answer(answer, guess):
    choix = ["A", "B", "C"]
    
    while True:
        if guess in choix:
            return 1 if guess == answer else 0
        
        guess = input(f"Choose: {choix} \n:==>").upper()
        if guess=="STOP":
            return -1
        
        
   


