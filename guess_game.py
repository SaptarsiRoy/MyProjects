
guess_number = 5
number = 0
print("Hello World")
while number != guess_number:
    number = int( input("Enter a number:"))
    if number == guess_number:
        print("You have guessed it right")
    else:
        print("Wrong guess try again")
