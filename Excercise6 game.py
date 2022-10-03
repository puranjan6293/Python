#Snake water gun game
#
# import random
# n=input("Enter your name\n")
# print("Welcome to snake water gun game\n",n)
# r=int(input("Enter the number of rounds you want to play\n"))
# rounds=1
# options=["s","w","g"]
# player_win=0
# computer_win=0
#
# while(rounds<=r):
#     print(f"round:{rounds}")
#     print("s for snake\ng for gun\nw for water")
#     player=input("Enter your choice\n")
#     if player !="s"and player !="g"and player !="w":
#         print("Invalid input,Please enter again")
#         continue
#     computer=random.choice(options)
#
#     if computer=="s":
#         if player=="g":
#             player_win +=1
#         elif player=="g":
#             computer_win +=1
#
#     if computer=="g":
#         if player=="s":
#             computer_win +=1
#         elif player=="w":
#             player_win +=1
#
#     if computer=="w":
#         if player=="s":
#             player_win +=1
#         elif player=="g":
#             computer_win +=1
#
#     if player_win>computer_win:
#         print("Congrats! You win this round",n)
#     elif player_win<computer_win:
#         print("Oops! You lose in this round",n)
#         print("Better luck next time")
#     else:
#         print("Round draw",n)
#     rounds+=1
#
#if player_win>computer_win:

#   print("Congrats! You win this game",n)

#     elif player_win<computer_win:
#         print("Oops! You lose the game",n)
#         print("Good luck next time")
#     else:
#         print("Match draw",n)
#     print("Your score:",player_win)
#     print("Computer score:",computer_win)
#
#     print("SEE YOU AGAIN",n)

#Right one
import random

n = input('Enter your name : ')
print('Welcome to our game ', n, '- Snake Water Gun')
r = int(input('Enter the number of rounds you wants to play : '))
rounds = 1
options = ['s', 'w', 'g']
player_win = 0
computer_win = 0

while rounds <= r:
    print(f"Round : {rounds}")
    print("Hit 's' for snake , Hit 'g' for gun , Hit 'w' for water")
    player = input('Choose your option : ')
    if player != 's' and player != 'g' and player != 'w':
        print('Invalid input! Please enter again')
        continue
    computer = random.choice(options)

    if computer == 's':
        if player == 'g':
            player_win += 1
        elif player == 'w':
            computer_win += 1

    if computer == 'g':
        if player == 'w':
            player_win += 1
        elif player == 's':
            computer_win += 1

    if computer == 'w':
        if player == 's':
            player_win += 1
        elif player == 'g':
            computer_win += 1

    if player_win > computer_win:
        print('Congarts!You win in this round', n)
    elif player_win < computer_win:
        print('Oops!You lose in this round', n)
        print('Better luck next time')
    else:
        print('Round draw!', n)

    rounds += 1

if player_win > computer_win:
    print('Congrats!You win the game', n)
elif player_win < computer_win:
    print('Oops!You lose the game', n)
else:
    print('Match draw!', n)
print('Your score : ', player_win)
print('Computer score : ', computer_win)



