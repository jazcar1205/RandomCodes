#Rock Paper Scissor Lizard Spock##
##Imports##
import random
import time 

##variables#
global options
options = ["rock","paper","scissor","lizard","spock"]
global cpu_guess 
global cpu_num
global user_guess 
global user_num
global cpu_score
cpu_score =0
global user_score
user_score =0
global re_play
global game_round
global player_1
global player_2
global user_g  
global player_1
global player_2

#functions# 
def  choices():
  global game_round
  global user_guess
  global user_num
  global user_g 
  game_round =1
  print("\n Welcome to Round: ",game_round," !\n")
  print(" type the character you want by inputing the number they are assigned \n rock : 0 \n paper: 1 \n scissor: 2\n lizard: 3 \n spock: 4 \n ")
  user_g = False
  user_guess = int(input("What do you choose?") )
  while( user_g != True):
    if (user_guess > 5):
      user_guess = options[int(input("What do you choose?") )]
    else:
      user_g = True
      user_num = user_guess
      user_guess = options[user_guess]
      time.sleep(3)
      print("\n ..... you choose...... ",user_guess,"\n" )
      game() 
    
def ways_to_win(player_1, player_2) :
  if (player_1 == 2 and (player_2 == 1 or player_2 == 3)):
    return True 
  elif(player_1 == 1 and (player_2 == 0 or player_2 == 4)):
    return True  
  elif(player_1 == 0 and (player_2 == 3 or player_2 == 2)):
    return True  
  elif(player_1 == 3 and (player_2 == 4 or player_2 == 1)):
    return True  
  elif(player_1 == 4 and (player_2 == 2 or player_2 == 0)):
    return True
  elif(player_1 == player_2):
    return "Tied"
  else:
    return False 

def game():
  global user_num
  global cpu_guess
  global cpu_num 
  global player_1
  global player_2
  cpu_guess = random.choice(options)
  cpu_num = options.index(cpu_guess)
  time.sleep(3)
  print("\n ..... the CPU choose...... ",cpu_guess,"\n" )
  player_1 = ways_to_win(cpu_num, user_num)
  player_2 = ways_to_win(user_num, cpu_num)
  update()
  
def update():
  global player_1
  global player_2
  global user_score
  global cpu_score
  global game_round 
  if(player_1 == True):
    cpu_score += 1 
    print(cpu_score)
    game_round += 1
  elif(player_2 == True):
    user_score +=1 
    game_round += 1
    print(user_score)
  elif(player_1 == "Tied" or player_2 == "Tied"):
    print("I was a Tie")
    choices()

##Start#
choices()