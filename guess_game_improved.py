print("This is a guessing game ")
input_num = None
guess_num = 5
chances = 3
while chances != 0 and input_num != guess_num:
    print("Entre a number:")
    input_num = int(input())
    if input_num == guess_num:
        print("Congratulations!!!!\nYou have guessed it correctly")
    else:
        print("Wrong guess!!! \nTry again")
        chances -= 1
        print(f"Chances left = {chances}")
if chances == 0:
    print("Better luck next time!!!")
