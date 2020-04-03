""" This is a game will play
the old fashioned rock, paper and scissor game"""
import random
import os
import time

choice = ["rock", "paper", "scissor"] #global list
#functiom for user input
def user_input():
    ip = None
    while ip not in [1, 2, 3]:
        ip = int(input("Rock, paper, scissor?(1, 2, 3)>>"))
        if ip not in [1, 2, 3]:
            print("Wrong input\n\n")
    return choice[ip - 1]


#function for computer input
def computer_input():
    return  choice[random.randint(1,3) - 1]

#function for replaying
def replay():
    return input("Do you want to play again?(y/n):") == 'y'

#main game starts here
usr_ip = None
comp_ip = None
total = 5
while True:
    playgame = input("Are you ready to play?(y/n):")
    if playgame == 'n':
        exit()
    usr_score = 0
    comp_score = 0
    while playgame == 'y':
        usr_ip = user_input()
        comp_ip = computer_input()
        if usr_ip == 'rock' and comp_ip == 'scissor':
            usr_score += 1
        elif usr_ip == 'scissor' and comp_ip == 'paper':
            usr_score += 1
        elif usr_ip == 'paper' and comp_ip == 'rock':
            usr_score += 1
        elif usr_ip == 'rock' and comp_ip == 'paper':
            comp_score += 1
        elif usr_ip == 'scissor' and comp_ip == 'rock':
            comp_score += 1
        elif usr_ip == 'paper' and comp_ip == 'scissor':
            comp_score += 1
        else:
            print("TIE")
        print("Your score:{0}\nComputer score:{1}".format(usr_score, comp_score))
        time.sleep(2)
        os.system("cls")
        if usr_score == total:
            print("You have won!!!")
            playgame = 'n'
        elif comp_score == total:
            print("Better luck next time :(")
            playgame = 'n'
    if not replay():
        break
