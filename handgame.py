import random

#function to input for cpu
def comp_decide():
    return random.randint(1,6)

#function to input for user
def user_decide():
    a = None
    while(True):
        print("Enter a number>>>")
        a = int(input())
        if a < 6 or a > 1:
            break
        print("Wrong input!!!")
    return a

#decide batting or bowling
def decide():
    a = random.randint(1,2)
    if a == 1:
        return ("batting", "bowling")
    else:
        return ("bowling", "batting")


#function to check if won
def checkwin(s1, s2):
    if s1 > s2:
        print("Congratulations!!! You have won\n\n\n")
    elif s1 < s2:
        print("Sorry!!! Better luck next time\n\n\n")
    else:
        print("Draw!!!\n\n\n")


#function for batting
def get_score(x, score):
    if x == "not out":
        a = user_decide()
        b = comp_decide()
        if a == b:
            print("You are out\nscore is {}\n\n\n".format(score))
            return get_score("out", score)
        else:
            score += a + b
            print("\nScore is {}\n\n".format(score))
            return get_score(x, score)
    else:
        return score



#main program
while(True):
    score1 = 0
    score2 = 0
    user, comp = decide()
    print("You will be {} first\n\n".format(user))
    if user == "batting":
        score1 = get_score("not out", 0)
        print("Computer's turn")
        score2 = get_score("not out", 0)
    else:
        score2 = get_score("not out", 0)
        print("Your turn")
        score1 = get_score("not out", 0)
    checkwin(score1, score2)
    print("Do you want to play again?(y/n):")
    replay = input().lower()
    if replay == 'n':
        break
