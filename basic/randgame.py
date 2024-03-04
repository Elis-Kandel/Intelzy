import random as rd
# a = rd.randint(1,6)
# print(a)
# try:
#     a=int(input("Enter a number"))
#     print(a)
# except Exception:
#     print("thats a string")
def main():
    print('\tNumber guessing game')
    comp_guess=rd.randint(1,10)

    while True:
        try:
            user_guess=int(input("\tEnter a number"))
        except Exception:
            print('Enter a valid number')
        if user_guess == comp_guess:
            print("Win!!")
            break
        elif user_guess > comp_guess:
            print("Lower")
        else:
            print("HIGHER")
            
main()