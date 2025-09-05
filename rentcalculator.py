rent= int(input("Enter your Room ren="))
food = int(input("enter the amount f food ordered = "))
electricity_spend = int(input("enter thr total of electricity spend ="))
charge_per_unit = int(input("Enter the charge per unit ="))
persons= int(input("Enter thr number of persons living in room="))

total_bill = electricity_spend * charge_per_unit

output = (food+rent+total_bill)// persons
print("each persons will pay= ", output)