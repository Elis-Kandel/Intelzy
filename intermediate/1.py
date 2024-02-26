import random as rd
lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/         O
               |         /|\\
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/         O
               |         /|\\
               |         /'\\
               |
            """,
        2: """
                ___________
               | /        | 
               |/         O
               |         /|\\
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/         O
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
lives=7
words=("donkey","monkey","buffalo","orangaton","tiger","elephant","giraffe","zebra","train","aeroplane","ship","bike","cycle","keyboard","monitor","mouse","printer","joystick","cauliflower","carrot","cabbage")
def used_word(guess,display):
    global lives
    if guess in display:
        print(f"{guess} is already used")
        lives-=1    
        print(f"remaining lives:-{lives}")
        print(display)

def guess_correctly(guess,letters,display,length):
    print(f" {guess} is a correct guess")
    position=0
    while position < length:
        if letters[position]==guess:
            display[position]=guess
        position+=1       
    print(f"remaining lives:-{lives}")
    print(display)
    
def not_guess_correctly(guess,display):
    global lives
    lives = lives -1
    print(f" {guess} is not a Correct guess ")
    print(f"remaining lives:-{lives}")
    print(display)
def playagain():
    global lives
    ans=input("enter y to continue ")
    if ans == "y":
        lives=7
        main()
    else:
       #lives=7 
       print("thank you for playing")
    
        
        
      
def main():
    randword=rd.choice(words).upper()
    length= len(randword)
    letters= list(randword)
    #print(letters)
    display=list("_"*length)
    print(display)
    while (lives != 0) and (display!=letters):
        print(lives_visual_dict[lives])
        guess=input(" Enter your guess:-  ").upper()
        if guess in letters:
            if  guess in display:
                used_word(guess,display)
            else:
                guess_correctly(guess,letters,display,length)
        else:
            not_guess_correctly(guess,display)
    if display==letters:
        print("you win")
    if lives== 0:
        print("you loose")
    playagain()
    

main()