#snake water gun game where snake = 1 , water = 0, gun = -1
import random

computer = random.choice([1 , 0 , -1])
print("Welcome To the Snake, Water, Gun game")
user = input("Enter your input (where snake:s, water:w, gun:g) : ")
userdict = {"s": 1 , "w" : 0 , "g": -1}
you = userdict[user]
reversedict = { 1 : "snake", 0 : "water" , -1 : "gun" }
print("Your input is " , reversedict[you], " and computer input is " ,reversedict[computer] )

if you == computer :
    print("Match is Draw")
else :
    if(you == 1 and computer == 0):
        print("You Won")
    elif(you == 1 and computer == -1 ):
        print("You Lose")
    elif(you == 0 and computer == 1 ):
        print("You Lose")
    elif(you == 0 and computer == -1 ):
        print("You Won")
    elif(you == -1 and computer == 0 ):
        print("You Lose")
    elif(you == -1 and computer == 1 ):
        print("You Won")
    else : 
        print("Something went wrong")
        
