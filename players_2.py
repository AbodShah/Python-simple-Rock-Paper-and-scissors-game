import termcolor
import getpass

firstplayer_wins = 0 
second_player_wins = 0 

# firstplayer_wins = firstplayer_wins + 1
# second_player_wins = second_player_wins + 1

def players_2():

 global firstplayer_wins
 global second_player_wins

 player_1 = getpass.getpass(" hey player 1! , choose one of Rock , Paper, Scissors  : ")
 termcolor.cprint("player 1 choosed " , color="light_green")
 player_2 = getpass.getpass(" hey player 2! ,  choose one of Rock , Paper, Scissors  : ")
 termcolor.cprint("player 2 choosed " , color="light_green")


# rock and rock
 if player_1.lower() == "rock" and player_2.lower() == "rock":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" No winnners : draw ")

# rock and paper
 elif player_1.lower() == "rock" and player_2.lower() == "paper":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_2 )
  second_player_wins = second_player_wins + 1
# rock and Scissors
 elif player_1.lower() == "rock" and player_2.lower() == "scissors":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_1)
  firstplayer_wins = firstplayer_wins + 1

# rock for first player done 
#########################################################################
 
 elif player_1.lower() == "scissors" and player_2.lower() == "scissors":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print("Draw")

 elif player_1.lower() == "scissors" and player_2.lower() == "rock":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_2)
  second_player_wins = second_player_wins + 1

 elif player_1.lower() == "scissors" and player_2.lower() == "paper":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_1)
  firstplayer_wins = firstplayer_wins + 1

##########################################################################

 elif player_1.lower() == "paper" and player_2.lower() == "paper":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print("Draw")

 elif player_1.lower() == "paper" and player_2.lower() == "scissors":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_2)
  second_player_wins = second_player_wins + 1

 elif player_1.lower() == "paper" and player_2.lower() == "rock":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_1)
  firstplayer_wins = firstplayer_wins + 1
#############################################################################

 elif player_2.lower() == "rock" and player_1.lower() == "rock":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" No winnners : draw ")

 elif player_2.lower() == "rock" and player_1.lower() == "paper":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_1)
  firstplayer_wins = firstplayer_wins + 1
 elif player_2.lower() == "rock" and player_1.lower() == "scissors":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_2)
  second_player_wins = second_player_wins + 1
#############################################################################


 elif player_2.lower() == "scissors" and player_1.lower() == "scissors":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print("Draw")

 elif player_2.lower() == "scissors" and player_1.lower() == "rock":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_2)
  second_player_wins = second_player_wins + 1

 elif player_2.lower() == "scissors" and player_1.lower() == "paper":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_1)
  firstplayer_wins = firstplayer_wins + 1
##############################################################################


 elif player_2.lower() == "paper" and player_1.lower() == "paper":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print("Draw")

 elif player_2.lower() == "paper" and player_1.lower() == "scissors":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_2)
  second_player_wins = second_player_wins + 1

 elif player_2.lower() == "paper" and player_1.lower() == "rock":
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  print(" Winner Is : " + player_1)
  firstplayer_wins = firstplayer_wins + 1
 else:
  print(" player 1 is: " + player_1 + "\n player 2 is: " + player_2)
  termcolor.cprint("Not Valid choice" , color="red")

 termcolor.cprint("Player 1 score is : " + str(firstplayer_wins) + "\n" "Player 2 score is : " + str(second_player_wins) + "\n" ,
  color="green")
 continue_game = input("Do you want to continue game ? send 'yes' if you want to continue and 'no' if you won't :  ")

 if continue_game == "yes":
  players_2()
 elif continue_game == "no":
   termcolor.cprint("Thanks for playing .. you quited" , color="yellow")
   quit()
 else: 
   termcolor.cprint("invalid input \n quited" , color="red")
   quit()

