import random 

secret_number = random.randint(10,100)


print(
"""Welcome To Verison """+str(int(secret_number/2))+""" of the game 
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess = int(input("What do you think the number is?"))
while( guess!= secret_number):
    print("Ha ha! You're stuck in my loop!")
    if(guess > secret_number):
        print("Your guess is to big \n")
    elif(guess < secret_number):
        print("Your guess is to small \n")
    guess = int(input("What do you think the number is?"))
print("--------Well done, muggle! You are free now.--------")