#Hand cricket game
import random

#function for computer input
def comp_decide():
    return random.randint(1,6)

#function for user input
def user_decide():
    inp = ' '
    while inp not in [1, 2, 3, 4, 5, 6]:
        inp = int(input("Enter numbrer(1-6)>>>"))
    return inp

#function to decide for batting or bowling
def decide():
    c = random.randint(1,2)
    if c == 1:
        return 'batting'
    else:
        return 'bowling'

def replay():
    print("Do you want to play again:")
    return input() == 'yes'
#main code

while(True):
    score1 = 0
    score2 = 0
    x = 0
    usr = decide()
    s = 'not out'
    print("You will {} first".format(usr))
    if usr == 'batting':
            while s == 'not out':
                a = comp_decide()
                b = user_decide()
                if a == b:
                    s = 'out'
                    print("You are out")
                else:
                    score1 += b
                    print("Score = {}".format(score1))
            print("Computer will bat")
            s = 'not out'
            while s == 'not out':
                a = comp_decide()
                b = user_decide()
                if a == b:
                    s = 'out'
                else:
                    score2 += a
                    print("Score = {}".format(score2))
                if score1 > score2:
                    print("You have won")
                    x = 1
                    break
                elif score1 < score2:
                    print("Better luck next time")
                    x = 1
                    break
    else:
            s = 'not out'
            while s == 'not out':
                a = comp_decide()
                b = user_decide()
                if a == b:
                    s = 'out'
                    print("Computer is out")
                else:
                    score2 += a
                    print("Score = {}".format(score2))
            print("You will bat")
            s = 'not out'
            while s == 'not out':
                a = comp_decide()
                b = user_decide()
                if a == b:
                    s = 'out'
                else:
                    score1 += b
                    print("Score = {}".format(score1))
                if score1 > score2:
                    print("You have won")
                    x = 1
                    break
                elif score1 < score2:
                    print("Better luck next time")
                    x = 1
                    break
    if x == 1 and score1 == score2:
        print("draw")
    if not replay():
        break
