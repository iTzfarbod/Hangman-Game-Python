
from random import *




def hangman(subject):
    


    n=randint(0,len(subject)-1)
    name=subject[n]

    charNumber=len(name)
    wrongs = 0
    userList=["-"]*charNumber    
    print(userList)



    while userList.count("-") > 0 :                   
        guess=input("guess a character: ")
        for i in range(charNumber):
            if guess == name[i]:
                userList[i]=guess
        if name.count(guess) == 0 :
            wrongs = wrongs + 1
            if wrongs != charNumber :
                print("no!! it's wrong. you have ",charNumber - wrongs , "more chances " )
            
        if wrongs == charNumber :
            print(" :( - you lose!1 " )
            print("the word was ",subject[n])
            break

        
        print(userList)
    if wrongs != charNumber :
        print(" :D - congrats - you win")
    else:
        exit()
