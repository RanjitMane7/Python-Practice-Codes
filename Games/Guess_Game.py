import random

print("..... GUESS GAME.....")
print("Your name please - ", end='')
name = input()

print("Hi " + name + "! \nwelcome to guess game")
print("now guess the number between 1 to 10... " + "\n" + name + "...don't forget you have 5 chances")

SecretNo = random.randint(1,10)
# print("DEBUG: Secret no is : " + str(SecretNo))

for No_of_guesses in range(1,6):
    print("\nwhat's your guess : ", end="")
    try:
        guessed_no = int(input())
        
        if guessed_no > SecretNo :
            print("thats high!")
        elif guessed_no < SecretNo :
            print("thats low!")
        else :
            break
    except ValueError :
        print(name + ", you didn't enter number!")

if guessed_no == SecretNo :
    print("Congrats " + name + ", you made it in " + str(No_of_guesses) + " chances.")
elif No_of_guesses == 5 :
    print("Hard luck! " + name + " you couldn't make it in 5 guesses")

        
