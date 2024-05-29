from Hangman import *

Games = ['fifa',"pes","mincrfat","callofduty","amoungus","fortnite","tetris",
         "arcade","needforspeed","ufc","pubg","freefire","mortalcombat",
         "hitman","nba","gta","reddeadramption","thelastofus","godofwar"]

Province = ['alborz','ardebil','bushehr','azarbaijan','esfahan','fars','gilan',
        'golestan','hamadan','hormozgan','ilam','kerman','kermanshah',
        'khuzestan','kordestan','lorestan','markazi','mazandaran','khorasan',
        'qazvin','qom','semnan','sistan','tehran','yazd','zanjan']

Food = ["pizza",'hamburger','hotdog',"taco", "salad", "ramen", "chocolate", "steak", "sushi", "ice cream", "pasta"]

Animal = ["cat","dog","lion","girafe","eagle","donkey","monkey","fish","shark",
          "horse","rabbit","cow","camel","sheep","bear","kangaroo",
          "goat","elephant","fox","duck","hen","wolf","tiger","pig"]



subject = [Province,Games,Food,Animal]

awnser = "y"
while awnser == "y" : 


    print("Select subject.")
    print("1.Provinces Of Iran ( 1 )")
    print("2.games ( 2 )")
    print("3.food ( 3 )")
    print("3.animal(english) ( 4 )")


 

    a = int(input(" choose  : 1,2,3,4 : "))


    hangman(subject[a-1])

    awnser = input(" do you want to continue ? y/n ")

    
