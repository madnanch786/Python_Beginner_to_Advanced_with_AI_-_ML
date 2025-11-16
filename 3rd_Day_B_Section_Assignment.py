'''
1. Take input in celcius and prints its equilent in Fahrenheit and kelvin ( Use explicit type conversion and arithmetic operators.)
formula:
Fahrenheit= (Cx9/5)+32
Kelvin=C+273.5
'''
celcius=float(input("Enter tempratue in Celcius: "))
fahrenheit=(celcius*9/5)+32
kelvin=celcius+273.5
print("Fahrenheit=",fahrenheit)
print("Kelvin=",fahrenheit)
'''
2. Write a program that take total bill aount and number of freinds as input.
calculate how uch each person will pay
also print he data type of each variable used
'''
totalBill=float(input("Please Enter the Total Bill: "))
totalFriends=int(input("Please Enter the Total No of Friends: "))
perFriendBill=float(round(totalBill/totalFriends,2))
print(f"Total Friends:{totalFriends}\nTotal Bill:{totalBill}\nBill Each will Pay: {perFriendBill} ")
print(f"Type of totalBill Variable:{type(totalBill)}\nType of totalFriend Variable:{type(totalFriends)}\nType of perFriendBill Variable: {type(perFriendBill)} ")