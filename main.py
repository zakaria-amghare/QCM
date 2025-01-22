from function import *
from users import *
clear_terminal()
name = input("what is your name? \n")
#verifier si le joueurs esr enregistrer sinon l'enregistrer
if is_player_registered(name)== True :
#si il est enregistrer on affiche les scores avec leurs date
       display_scores(name)
else:
#sinon enregistrer le joueurs
       register_player(name)

#hadi ki dir la partie ta3ak zaki tahsablou score ou dakhlou m3a assam joueurs bach t'enregistrih
add_score(name,new_game())
display_scores(name)