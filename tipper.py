#MAIN MODULE
#call INPUT MODULE
#call CALCULATIONS
#call OUTPUT MODULE
#INPUT MODULE
SalesAmmount = input("Enter_sales_ammount_for_the_purchase.")
SalesAmmount = float(SalesAmmount)
########Tip the percentage for the name
Tip1 = (.15)
Tip1 = float(Tip1)
Tip2 = (.2)
Tip2 = float(Tip2)
#CALCULATIONS
EmpEarned1 = (Tip1 * SalesAmmount)
EmpEarned2 = (Tip2 * SalesAmmount)
#OUTPUT MODULE
print ("The_profit_for_employee_is_with_15%_is_$" + str(EmpEarned1) + ".")
print ("The_profit_for_employee_is_with_20%_is_$" + str(EmpEarned2) + ".")
print ("Rootbeer is great.")
print("""
.~~~~.
i====i_
|cccc|_) root
|cccc|   beer
`-==-'   
""")
