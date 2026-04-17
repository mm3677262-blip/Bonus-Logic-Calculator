discount = 0.0
bill = float(input("Enter the total bill amount: "))
if  bill % 2 == 0 and bill > 50 : #did the user enter an even number?
    print("Even bill amount! You get a bonus discount! 🎉")
elif bill % 2 != 0 or bill < 50: #did the user enter an odd number or a bill less than 50?
    print(" No bonus discount this time. 😕 because the bill is not even or not greater than 50.")    
if bill > 100:
    discount = 0.20
elif 50 <= bill <= 100: #edited the condition to include 50 and 100
    discount = 0.10
else: 
    discount = 0.0
if bill % 2 == 0 and bill > 50: #added the condition to check if the bill is greater than 50 and even number
    discount += 0.05
    print("Bonus discount applied! 🎁")
print(f"Initial discount: {discount*100:.2f}%") #display the initial discount percentage
print(f"Final bill amount after discount: {bill * (1 - discount):.2f}") #display the final bill amount after applying the discount