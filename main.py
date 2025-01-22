import time
from function import *
from users import *
clear_terminal()
name = input("what is your name? \n")
#verifier si le joueurs esr enregistrer sinon l'enregistrer
if is_player_registered(name)== True :
#si il est enregistrer on affiche les scores avec leurs date
       display_scores(name)
       input("Press Enter to continue...")
       clear_terminal()
else:
#sinon enregistrer le joueurs
       register_player(name)


# Load the JSON file
choix = ["1", "2", "3","4"]

#hadi ki dir la partie ta3ak zaki tahsablou score ou dakhlou m3a assam joueurs bach t'enregistrih
category='0'
while True:
       if category in choix:
              break
       print('1-Mathematics')
       print('2-Physics')
       print('3-Chemistry')
       print('4-History')
       category=input("\nwhat cotegorie do you want to do?")
       clear_terminal()


if category=='1':category='Mathematics' 
if category=='2':category='Physics' 
if category=='3':category='Chemistry' 
if category=='4':category='History' 
start_time = time.time()
add_score(name,new_game(category),category)
end_time = time.time()
clear_terminal()
elapsed_time = end_time - start_time
minutes, seconds = divmod(elapsed_time, 60)
print(f"\nQuiz completed in {int(minutes)} minutes and {int(seconds)} seconds.")
input("Press Enter to see the histotyque...")
clear_terminal()
display_scores(name)