import random as rd
from datetime import datetime,timedelta
def game():
    currentTime=datetime.now()
    print("\t Guess game")
    THRESOLD=0
    computer_number=rd.randint(1,100)
    while True:
        if currentTime<datetime.now()-timedelta(seconds=2):
            print("TIME UP")
            break
        try:
            guess= int(input("Enter a number"))
        except Exception:
            print("Try entering a number")
            continue
        
        if guess == computer_number:
            print("you Win")
            break
        elif guess < computer_number:
            THRESOLD=computer_number-guess
            if THRESOLD > 4:
                print("Too low")
            else:
                print("Low")
        else:
            THRESOLD=guess-computer_number
            if THRESOLD > 4:
                print("Too high")
            else:
                print("High")
game()