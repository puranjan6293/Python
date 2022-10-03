"""

#Guess the number

n1=18
print("You can guess only 9 times\nSo be carefull")
while(True):
    n2=int(input("Guess any number\n"))
    if n2<18:
        print("Thoda aur jyada koro")
    elif n2>18:
        print("Thoda aur kom koro")
    else:
        print("Congratulations\nYour guess is right")
        break



#Advance one
n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")

"""
#Lets make a Guess game

n1=18
print("Hii sir\n Could you please guess any no?\n")
print("But remember you have only 9 chance\n")
n2=1
while(n2<=9):
    n3=int(input("Guess any no\n"))
    if n3<18:
        print("Sir thoda aur jyada no daliye\n")
    elif n3>18:
        print("Sir thoda aur kom no daliye\n")
    else:
        print("Congratulations Sir\nYour guess is correct\n You won!\n")
        print(n2,"no.of guess you took to finish this game\n")
        break
    print(9-n2,"Number of guess left\n")
    n2=n2+1
if n2>9:
    print("Game over\n Sorry sir")

