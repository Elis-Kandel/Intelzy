import random as rd
rand_word = ["Computer"]
# rand_word = rd.choice(word)
print(rand_word)
len = len(rand_word)
upr = rand_word.upper()
display = []
for i in rand_word:
    display += ""
print(display)

def check():
    ask = input("enter any letter:  ").upper()
    print(ask)
    for i in upr:
        if ask == i:
            print(word.index(ask))
            print('nice')


check()