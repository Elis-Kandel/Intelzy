import random as rd
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board']
def game():
    comp_number=rd.randint(0,11)
    comp_word=words[comp_number]
    print(comp_word)
    while True:
        turn=3
        while turn!=0:
            guess=str(input("Enter your guess"))
            if guess == comp_word:
                print("Win")
                break
            else:
                print("Not right")
                turn=turn-1
        print("You failed") 
        break
        
        
game()
