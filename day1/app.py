# Send repo to: chandra.ayodhya@smoothstack.com
from math import ceil

#1
print(50 + 50)
print(100 - 10)

#2
print("30+*6 doesn't work.")
print(6^6)
print(6 ** 6)
print(6 + 6 + 6 + 6 + 6 + 6)

#3
print("Hello World")
print("Hello World : 10")

#4
p = int(input("What is your principle balance?"))
r = int(input("What is your interest rate?")) / 100
l = int(input("How many months is your loan?"))

monthly_payment = (r / 12) * (1 / (1 - (1 + r / 12) ** (-l))) * p
print(ceil(monthly_payment))