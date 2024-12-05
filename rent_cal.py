# Rent Calculator
total_rent = int(input("Enter the total rent ="))
food = int(input("Enter the total food charges ="))
water = int(input("Enter the total water charges ="))
elec_charges = int(input("Enter the total electricity charges ="))
person = int(input("Enter the number of person living in room ="))

total_Amount = (total_rent + food + water + elec_charges) // person
print("Each person will pay =",total_Amount)