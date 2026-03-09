import random as r
import time
def game(res):
    '''Reply in 1 or 2 or 3'''
    def Snake():
        if l2[res] == "Snake🐍"and m == "Water🌊":
          print("Snake🐍 beats the Water🌊\n")
          time.sleep(1)
          print("You Win🥳")
          exit()
        else:
          print("Gun🔫 beats the Snake🐍\n")
          time.sleep(1)
          print("You Lose😔")
          exit()
     
    def Water():
       if l2[res] == "Water🌊" and m == "Gun🔫":
          print("Water🌊 beats the Gun🔫\n")
          time.sleep(1)
          print("You Win🥳")
          exit()
       else:
          print("Snake🐍 beats the Water🌊\n")
          time.sleep(1)
          print("You Lose😔")
          exit()
    def Gun():
         if l2[res] == "Gun🔫" and m == "Snake🐍":
            print("Gun🔫 beats the Snake🐍\n")
            time.sleep(1)
            print("You Win🥳")
            exit()
         else:
            print("Water🌊 beats the Gun🔫\n")
            time.sleep(1)
            print("You Lose😔")
            exit()     
           
        
    l1 = ["Snake🐍", "Water🌊", "Gun🔫"]
    l2 = {0: 0, 1: "Snake🐍", 2: "Water🌊", 3: "Gun🔫"}
    m = r.choice(l1)
    print("You Chose:",l2[res])
    time.sleep(1)
    print("System Chose:",m)
    time.sleep(1)
    if l2[res] == m:
        print("Game Tied😏")
        exit()
    if l2[res] == "Snake🐍":
        Snake() 
    if l2[res] == "Water🌊":
        Water() 
    if l2[res] == "Gun🔫": 
        Gun()
        

print("Welcome To The Snake🐍 Water🌊 Gun🔫 Game")
print()
time.sleep(1)
print("Select: 1.Snake🐍 or 2.Water🌊 or 3.Gun🔫")
print()
time.sleep(2)
print(game.__doc__)
print()
res = int(input())
game(res)