import getpass
import random
import computergames 
import termcolor
import players_2
# Rock , Paper, scissors, 
# rock win Scissors
# Scissors win Paper 
# Paper win rock

termcolor.cprint("welcome to  Rock, Paper, Scissors game ..." , color="blue" , end="\n\n")

start_game = input("Do you want to play with copmuter (1 player) or freind (2 players ) ? \n\n send 1 to play Vs copmuter and \n send 2 to play with a freind  :")
if start_game.lower() == "2": 
 termcolor.cprint("okey let's play \n" , color="blue")
 players_2.players_2()
 

elif start_game.lower() == "1" : 
  computergames.computergame()
  quit()
else:
 termcolor.cprint("invalid choice .. please type 1 or 2 only " , color="red")
 quit()

 ################################## 