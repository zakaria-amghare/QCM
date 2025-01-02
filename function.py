import json
with open("questions.json","r") as file:
    globaldata=json.load(file)

def new_game():
    player=input("what is your name:")
    scor=0
    question_number=1
    localdata=globaldata["QUIZ"]
    for question in localdata:
        print(f"{question_number}"+") "+question["question"])
        for option in question["options"]:
            print(option)
        guess=input("choose:")
        guess=guess.upper()
        result=check_answer(question["answer"], guess)
        if result==1:
            scor=scor+result
        elif result== -1:
            break
        question_number=question_number+1
    print("you have:"+f"{scor}"+"piont")
    

def check_answer(answer, guess):
    choix = ["A", "B", "C", "D"]
    yes_no = ["YES", "NO"]
    
    while True:
        if guess in choix:
            return 1 if guess == answer else 0
        
        guess = input(f"Choose: {choix} \n:==>").upper()
        if guess=="STOP":
            return -1
        
   


new_game()