
import random
ch=("R","P","S")
computer=random.choice(ch)
print("----------------------------------")
print("=====ROCK-PAPER-SCISSORS-GAME=====")
print("----------------------------------")
def r_p_s_game(u_num,c_num):
    while True:
        user="a"
        while user not in ch:
            uc= input("enter 'R' for ROCK, 'P' for PAPER and 'S' for SCISSORS\n----------------------------------\n")
            user=uc.upper()
            print(f"=====Player: {user}=====\n=====Computer: {computer}=====")
            #print(user)
        if user == computer:
            print("=====TIE=====")
            u_num+=1
            c_num+=1
        elif(user == "R" and computer == "S"):
            print("=====YOU WIN=====")
            u_num+=1
        elif (user == "S" and computer == "P"):
            print("=====YOU WIN=====")
            u_num+=1
        elif (user == "P" and computer == "R"):
            print("=====YOU WIN=====")
            u_num+=1
        else:
            print("=====YOU LOOSE=====")
            c_num+=1
        print("----------------------------------")
        print("=====SCORE=====") 
        print(f"--------------USER: {u_num}") 
        print(f"--------------COMPUTER: {c_num}")
        print("\n----------------------------------")
        cont=input("=====DO YOU WANT TO CONTINUE(Y/N)=====").upper()
        if cont=="Y":
            r_p_s_game(u_num,c_num)
        else:
            print(f"FINAL SCORE \n PLAYER: {u_num}\n COMPUTER: {c_num} ")
            if u_num> c_num:
                 print("======YOU WIN=====")
            if u_num== c_num:
                print("=====TIE=====")
            if u_num< c_num:
                print("=====YOU LOOSE=====")
            break
r_p_s_game(0,0)