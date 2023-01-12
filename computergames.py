import random
import termcolor

player_wins = 0
copmuter_wins = 0 


def computergame(): 
 
 player = input(" hey , choose one of Rock , Paper, Scissors  : ")
 options = ["rock" , "paper", "scissors"]
 random_number = random.randint(0,2)
 computer_choice = options[random_number]
 
 
 global player_wins
 global copmuter_wins

 if computer_choice == "rock" and player.lower() == "rock" : 
   print("Draw")



 elif computer_choice == "paper" and player.lower() == "rock" : 
   print("You Lose ):")
   copmuter_wins = copmuter_wins + 1 


 elif computer_choice == "scissors" and player.lower() == "rock" : 
   print("You Win (:")
   player_wins = player_wins + 1

   
 elif computer_choice == "scissors" and player.lower() == "paper" : 
  print("You lose (:")
  copmuter_wins = copmuter_wins + 1 

 elif computer_choice == "paper" and player.lower() == "paper" : 
   print("draw")


 elif computer_choice == "rock" and player.lower() == "paper" : 
   print("You Win (:")
   player_wins = player_wins + 1

 elif computer_choice == "paper" and player.lower() == "rock" : 
  print("You lose (:")
  copmuter_wins = copmuter_wins + 1 


 elif computer_choice == "rock" and player.lower() == "rock" : 
   print("draw")


 elif computer_choice == "scissors" and player.lower() == "rock" : 
   print("You Win (:")
   player_wins = player_wins + 1
 else :
  print("invalid input")
 
 termcolor.cprint( "Your score is : " + str(player_wins) + "\n" "computer score is : " + str(copmuter_wins) + "\n" , color="green")

########################################################################

 continue_game = input("Do you want to continue game ? send 'yes' if you want to continue :  ")

 if continue_game == "yes":
  computergame()
 elif continue_game == "no":
   termcolor.cprint("Thanks for playing .. you quited" , color="yellow")
   quit()
 else: 
   termcolor.cprint("invalid input \n quited" , color="red")
   quit()

