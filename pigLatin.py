#pig latin
letter_pos = None
def pig_latin(word):
    i = 0
    for item in word:
        if item in 'aeiou':
            letter_pos = i
        else:
            i+=1
    pig_word = word[letter_pos:] + word[0:letter_pos] + "ay"
    return pig_word
print("Enter a word:")
user_word = input()
print("Pig latin form is {}".format(pig_latin(user_word)))
