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
        if check_answer(question["answer"],guess)!=-1:
            scor=scor+check_answer(question["answer"],guess)
        else:
            print("you have:"+f"{scor}"+"piont")
            break
        question_number=question_number+1
    print("you have:"+f"{scor}"+"piont")


def check_answer(answer,guess):
    choix=["A","B","C","D"]
    yes_no=["YES","NO"]
    while True:
        if guess not in choix:
            print(" do you wish to continue")
            while True:
                print("====>YES")
                print("====>NO")
                continue_the_quizz=input("--->")
                continue_the_quizz=continue_the_quizz.upper()
                if continue_the_quizz in yes_no:
                    break
            if continue_the_quizz=="YES":
                guess=input("choose:"+f"{choix}" )
                guess=guess.upper()
                break
            else:
                print("thanks for playing with us!")
                return -1

        else:
            if answer==guess:
                return 1
            else:
                return 0


new_game()