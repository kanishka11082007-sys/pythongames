import random
print("Welcome to the perfect guess game")
print("you'll have to guess the number from your chosen limits")
a=int(input("enter lower limit: "))
b=int(input("enter higher limit: "))
print("start guessing the number!")
computer=random.randint(a,b)
if (b-a)>=1 and (b-a)<=5:
    print("you have only 1 chance to guess!")
elif (b-a)>5 and (b-a)<=15:
    print("you have only 3 chance to guess!")
elif (b-a)>15 and (b-a)<=40:
     print("you have only 5 chance to guess!")
elif (b-a)>40 and (b-a)<=100:
    print("you have only 7 chance to guess!")
for i in range(7):
    gss=int(input("enter your guess: "))
    if gss>computer:
        print("no is high aim for lower")
    elif gss<computer:
        print("no. is low aim for higher ")
    elif gss==computer:
        print("you guessed the no in",i+1,"guess")
        break
    else:
        print("theres some error with the program")
    
    
    