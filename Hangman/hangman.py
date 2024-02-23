word='dora'
display=[]
for i in word:
    display+="_"
def user_input(chance=5):
    letter=""

    while chance>0:
        
        if display == [*word]:
            print("Win")
            exit()
        else:  
            print('''
              Guessing a letter
              ''')
            letter=input()
            for i in word:
                if letter == i:
                    index=word.index(i)
                    display[index] = i
                    print(display)
                    user_input(chance)
            
            for i in word:
                if letter!=i:
                    chance-=1 
                    print(f"you have{chance} left")
                    break
                    
            if chance==0:
                print("You lose")
                break
            
            
user_input()