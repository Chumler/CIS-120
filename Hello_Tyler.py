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
# This is a one line note
'''
#***************************************************************
'''
This is a multiple lined note.
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
SalesAmmount = input("SalesAmmountEnter_sales_ammount_for_the_month.")
SalesAmmount = float(SalesAmmount)
ComRate = input("Enter_commission_rate_as_a_decimal.")
ComRate = float(ComRate)
#CALCULATIONS
EmpEarned = (ComRate * SalesAmmount)
#OUTPUT MODULE
print ("The_profit_for_employee_is_" + str(EmpEarned))
'''
#***************************************************************
