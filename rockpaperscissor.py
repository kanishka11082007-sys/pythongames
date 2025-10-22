import random
userchoice = input("Rock, Paper, scissors (r/p/s)? : ")
choice = ('r', 'p', 's')

dict1 = {'r': 1, 'p': 0, 's': -1}
revdict = {1: 'Rock', 0: 'Paper', -1: 'Scissor'}
if userchoice not in choice:
    print("invalid choice")
else:
    you = dict1[userchoice]
    computer = random.randint(-1, 1)
    if revdict[you] == 'Rock':
        print("You chose ", revdict[you], '🪨')
    elif revdict[you] == 'Paper':
        print("You chose ", revdict[you], '📃')
    elif revdict[you] == 'Scissor':
        print("You chose ", revdict[you], '✂️')
    if revdict[computer] == 'Rock':
        print("computer chose", revdict[computer], '🪨')
    elif revdict[computer] == 'Paper':
        print("computer chose", revdict[computer], '📃')
    elif revdict[computer] == 'Scissor':
        print("computer chose", revdict[computer], '✂️')
    if revdict[you] == 'Rock' and revdict[computer] == 'Paper':
        print("You lose!")
    elif revdict[you] == 'Rock' and revdict[computer] == 'Scissor':
        print("You won!")
    elif revdict[you] == 'Scissor' and revdict[computer] == 'Paper':
        print("You won!")
    elif revdict[you] == 'Scissor' and revdict[computer] == 'Rock':
        print("You lose!")
    elif revdict[you] == 'Paper' and revdict[computer] == 'Rock':
        print("You won!")
    elif revdict[you] == 'Paper' and revdict[computer] == 'Scissor':
        print("You lose!")
    elif revdict[you] == revdict[computer]:
        print("It's a draw!")
