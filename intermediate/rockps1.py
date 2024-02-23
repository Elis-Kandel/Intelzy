import random as rd
spr={
    '1':'Rock','2':'Paper','3':'Scissors'
}
print("""
            Choose one of the following:
            1: Rock
            2: Paper
            3: Scissors
      """)
def get_user_choice():
    user_choice='0'
    while user_choice not in ['1','2','3']:
        user_choice = input("Enter your choice: ")
    spr_list=["Rock","Paper","Scissor"]
    comp_choice=rd.choice(spr_list)
    print("user choice is", spr[user_choice])
    print("Computer choice is",comp_choice)
    return user_choice,comp_choice
def check_winner(comp_choice,user_choice):
    if user_choice==comp_choice:
        result="Tie"
    if user_choice.lower() is 'rock':
        if comp_choice.lower() is 'paper':
            result="You lose"
        else:
            result="You win"
    elif user_choice.lower() is 'paper':
        if comp_choice.lower() is 'rock':
            result="You win"
        else:
            result="You lose"
    else:
        if comp_choice.lower() is 'paper':
            result="You win"
        else:
            result="You lose"
    print(result)  
def game():  
    while True:
        user_choice,comp_choice=get_user_choice()
        check_winner(user_choice,comp_choice)
        again=input("Do you want to continue(y/n)")
        if again.lower() == 'y':
            game()
        elif again.lower() == 'n':
            break
    
game() 