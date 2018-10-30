print ("""
.~~~~.
i====i_
|cccc|_) root
|cccc|   beer
`-==-'   
""")
#***************************************************************
'''
Programmer: Tyler G.
Date: September 20,2018
Program: Hello_Tyler
'''
#***************************************************************
'''
name = ("Tyler Goodman")
greeting = ("Hello " + name)
greeting += (", welcome")
print (greeting)
'''
#***************************************************************
'''
print ("What is your favorite animal?")
favAnimal = input ()
print ("I like the " + favAnimal + " as well. ;) ")
favAnimal = input("What is your favorite animal?\n")
print ("I like the " + favAnimal.upper() + " as well. ;) ")
'''
#***************************************************************
'''
dogAge = input("How old is your dog?")
print (type(dogAge))
dogAge = int(dogAge)
humanYears = dogAge * 7
print (humanYears)
'''
#***************************************************************
'''
#MAIN MODULE
#call INPUT MODULE
#call CALCULATIONS
#call OUTPUT MODULE
#INPUT MODULE
SalesAmmount = input("Enter_sales_ammount_for_the_month.")
SalesAmmount = float(SalesAmmount)
ComRate = input("Enter_commission_rate_as_a_decimal.")
ComRate = float(ComRate)
#CALCULATIONS
EmpEarned = (ComRate * SalesAmmount)
#OUTPUT MODULE
print ("The_profit_for_employee_is_" + str(EmpEarned))
'''
#***************************************************************
'''
#MAIN MODULE
#call INPUT MODULE
#call CALCULATIONS
#call OUTPUT MODULE
#INPUT MODULE
Males = input("Enter_ammount_of_males.")
Males = int(Males)
Females = input("Enter_ammount_of_females.")
Females = int(Females)
#CALCULATIONS
MaleOverFem = (Males / Females)
FemOverMale = (Females / Males)
#OUTPUT MODULE
print ("The_percentage_for_males_to_females_is_" + str(MaleOverFem))
print ("The_percentage_for_females_to_males_is_" + str(FemOverMale))
'''
#***************************************************************
'''
#DECLARE VARIABLE
SongNum = 0
SongPrice = .99
TotalPrice = 0.0
#INPUT
SongNum = int(input("Input number of songs for purchase? "))
#PRINT
if (SongNum >= 20):
    TotalPrice = SongNum * SongPrice
elif (SongNum >= 9):
    TotalPrice = SongNum + SongPrice
else:
    TotalPrice = SongNum * SongPrice
TotalPrice = TotalPrice - (TotalPrice *.05)
#OUTPUT
print("The_number_of_songs_you_want_to_purchase_is", SongNum)
print("The_total_price_for_your_purchase_is_$", TotalPrice)
'''
#***************************************************************
'''
Num = int(input("Input_a_number."))
if (Num > 0):
    print ("This_is_positive.")
elif (Num < 0):
    print ("This_is_negative.")
else:
    print ("This_equals_0.")
'''
#***************************************************************
'''
HodDogRemainder = 0
DogPacks = 0
PacksNeeded = 0
PeopleThere = int(input("""How_many_people_?
"""))
PeopleDogs = int(input("""How_many_hot_dogs_Are_you_giving_each_person?
"""))

PacksNeeded = int((PeopleDogs*PeopleThere)/ 8)
HotDogRemainder = (PeopleDogs % 8)
print ("You_need",PacksNeeded,"packages.")
print ("You_will_have", PeopleDogs, "leftover.")
'''
#***************************************************************
'''
counter = 0
while (counter < 5):
    print(counter)
    counter += 1
print ("All_done.")
'''
#***************************************************************
'''
flag = False
while flag == False:
    print ("This_flag_is_false.")
    flag = True
'''
#***************************************************************
'''
playAgain = 'y'
while playAgain == 'y':
    print ("You_are_inside_the_loop.")
    playAgain = input("Do_you_want_to_play_again?")
    playAgain = playAgain.lower()
print ("Thanks_for_playing!")
'''
#***************************************************************
'''
numTimes = 0
playAgain = 'y'
while playAgain == 'y':
    print ("You are in the loop")
    playAgain = input("Do_you_want_to_play_again?")
    playAgain = playAgain.lower()
    numTimes += 1;
    print ("This_is_loop_number",numTimes,".")
print ("Thanks_for_playing!")
'''
#***************************************************************
'''
grades = 0.0
gpa = 0.0
numGrades = 0
totgrades = 0.0

while (grades >= 0):
    print ("Enter grade please.")
    grades = float(input("""Input a negative number to quit.
"""))
    print ("Before add",totgrades)
    if (grades >= 0):
        totgrades += grades
        numGrades += 1
    print ("After add", totgrades)
print ("Total grades entered is", numGrades)
print ("Total average of grades is", totgrades/numGrades)
print ("Thanks for testing the program. ;)")
'''
#***************************************************************
'''
DayBugs = 0
TotBugs = 0
BugNum = 0
DayNum = 1
while (DayNum <= 5):
    DayBugs = int(input("""How many bugs did you catch today?
"""))
    TotBugs += DayBugs
    DayNum += 1
print ("You have caught a total of", TotBugs, "bugs.")
'''
#***************************************************************
'''
num = 0.0
totnum = 0.0
while (num >= 0):
    num = float(input("""Please input a positive number.
"""))
    if(num >= 0):
        totnum += num
        print (num,"is a positive number.")
    else:
        print ("that leaves your total to",totnum)
'''
#***************************************************************
'''
import random
somenum = 101
for x in range(0,somenum,25):
    num = random.randint(1,101)
    print(num)
    print(x)
    num = random.randint(1,101)
    print(num)
'''
#***************************************************************
'''
import random
tot = 0
day = 0
num = random.randint (0,50)
for x in range(num):
    bugs = random.randint (5,25)
    tot += bugs
    day += 1
    print(bugs,"bugs on day",day)
    print(tot,"as a total")
'''
#***************************************************************
'''
TotalScore = 0
Grades = 0
NumGrades = int(input("Please enter ammount of grades to be entered"))
for x in range(NumGrades):
    Grades = int(input("Grade: "))
    TotalScore += Grades
print (TotalScore)
'''
#***************************************************************
'''
import random
count1 = 0
count2 = 0
play1 = random.randint (2,15)
play2 = random.randint (2,15)
for x in range(15):
    while (play1 == play2):
        print("score for player 1 is",play1,"and player 2 has a score of",play2)
        print("you tied")
    if (play1 > play2):
        if (count1 < 15):
            print("score for player 1 is",play1,"and player 2 has a score of",play2)
            count1 += 1
        else:
            print("player 1 wins")
    else:
        if (count1 < 15):
            print("score for player 1 is",play1,"and player 2 has a score of",play2)
            count2 += 1
        else:
            print("player 2 wins")
'''
#***************************************************************
'''
UserWord = input("Enter a word here.")
CurIndex = 0
OtherWord = ''
for c in UserWord:
    if (CurIndex / 2 == 0):
        OtherWord += c.lower()
    else:
        OtherWord += c.upper()
    CurIndex += 1
print (OtherWord)
'''
#***************************************************************
'''
List = ["Cherries","apples","plums","bells","melons","bars"]
for x in range(0,6,2):
    print (List[x])
'''
#***************************************************************
'''
import random
List = ["Cherries","apples","plums","bells","melons","bars"]
Ran = random.randint(0,5)
print (List[Ran])
'''
#***************************************************************
A1 = str(input("""Please input your first alphanumeric input.
"""))
A2 = str(input("""Please input your second alphanumeric input.
"""))
A3 = str(input("""Please input your third alphanumeric input.
"""))
List = [A1,A2,A3]
print (List)
















































































































































































