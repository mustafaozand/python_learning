# Calculating Mobile Phone Costs
# date: 03/05/2021

username = input("Enter Name and Surname:")

print()
print ("Welcome",username,)
print()
print("To check the total amount of money you have spent please answer the questions below")

minutes_talked = input("How many minutes have you talked on the phone this month?:")
minutes_cost = float(minutes_talked) * 0.10

number_of_texts = input ("How many texts have you sent in a month:")
texts_cost = float(number_of_texts) * 0.05


bill_amount = minutes_cost + texts_cost 

print ("Bill Amount of the month = £{0}".format(bill_amount))

vat = bill_amount * 0.20

bill_amount_with_vat = bill_amount + vat

print("Bill Amount with VAT = £{0}".format( bill_amount_with_vat ))
