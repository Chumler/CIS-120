import random
Username = str(input("""Hi, my name is Hal.
Could you please tell me yours?
ENTER YOUR NAME: """))
TheNum = int(input("Its nice to meet you " + Username + """.
Could you please note a whole number from 1 to 100.
Im going to try to guess it.
ENTER A NUMBER: """))
LowNum = 0
HighNum = 100
GuessCount = 0
GuessNum = int(0)
while (TheNum != GuessNum):
    GuessNum = random.randint(LowNum,HighNum)
    GuessCount += 1
    if (GuessNum > TheNum):
        print ("Is", GuessNum, "your number?")
        a = str(input("Is it higher or lower?"))
        HighNum = GuessNum
    if (GuessNum < TheNum):
        print ("Is", GuessNum, "your number?")
        a = str(input("Is it higher or lower?"))
        LowNum = GuessNum
    if (GuessNum == TheNum):
        print ("Is", GuessNum, "your number?")
        print ("this took me", GuessCount, "tries.")
        
