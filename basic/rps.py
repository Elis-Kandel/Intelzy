import random as rd
def game():
    while True:
        main()
        break
def main():
    
    choice=['rock','paper','scissor']
    chance=3
    wins={
        "user_win":0,
        "comp_win":0
    }
    # Computer choice
    
    print("-------Rock---Paper---Scissord-------")
    # user choice
    while True:
        while chance>0:
            a=input()
            user_choice=a.lower()
            if user_choice not in choice:
                print("Please type Rock, Paper or Scissor")
                continue
            else:
                chance-=1
                moves=[0,1,2]
                comp_choice=rd.choice(moves)
                if comp_choice == 1:
                    print("paper")
                elif comp_choice==0:
                    print("rock")
                else:
                    print("scissor")
                
                if user_choice is 'rock':
                    if comp_choice == 0:
                        continue
                    elif comp_choice == 1:
                        wins["comp_win"]+=1
                    else:
                        wins["user_win"]+=1
                elif user_choice is 'paper':
                    if comp_choice == 1:
                        continue
                    elif comp_choice == 2:
                        wins["comp_win"]+=1
                    else:
                        wins["user_win"]+=1
                else:
                    if comp_choice == 2:
                        continue 
                    elif comp_choice == 0:
                        wins["comp_win"]+=1
                    else:
                        wins["user_win"]+=1    
                
        #to check final win
        if wins["comp_win"] is not wins["user_win"]:
            if wins["comp_win"] > wins["user_win"]:
                diff=wins["comp_win"]-wins["user_win"]
                print(f"Computer wins by {diff}")
                
            else:
                diff=wins["user_win"]-wins["comp_win"]
                print(f"You win by {diff}")
                
                    
        else:
            print(f"Toss{wins['comp_win']} {wins['user_win']}")   
                
        b=input("Do you want to continue?(y/n)")
        game=b.lower()
        if game == 'y':
            main()
        else:
            break
    
            
                
                    
            
                
                        
                    
                    
                    
                    
            
        
game()