#Finance Calculators - A program that calculate investment return and fixed-rate mortgage repayment 
#How it works:
#1.Showing the choices to the user
#2.Prompt user for choice of calculation
#3.If the user chooses investment, prompt the user to enter the relevant details and select the method to calculate the interest
#4.If the user chooses mortgage, prompt the user to enter the relevant details and calculate the monthly repayment
#5.Display the result to the user
#------Clean--------------------------------------------------------------

#import math module for power function
import math

# Showing the choices to the user
print("investment - to calculate the amount of interest you will earn on your investment")
print("mortgage       - to calculate the amount you'll have to pay on a home loan")
separator = "                                                                        "
print(separator)

# Prompt user for choice of calculation
choice = input("Enter either 'investment' or 'mortgage' from the menu above to proceed:")

# if the user chooses investment
if choice.lower() == 'investment':
    principal = float(input("Enter the amount of money that you are depositing: £"))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    time = float(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' interest? ")

    if interest.lower() == 'simple': # if the user chooses simple
        total_amount = principal * (1 + rate * time)
        print("Total amount after interest: ""£", total_amount)
    elif interest.lower() == 'compound': # if the user chooses compound
        total_amount = principal * math.pow((1 + rate), time)
        print("Total amount after interest: ""£", total_amount)
    else:
        print("Invalid choice. Please enter 'simple' or 'compound'.")

# if the user chooses mortgage
elif choice.lower() == 'mortgage':
    present_value = float(input("Enter the present value of the house: £"))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100 / 12  # Monthly rate
    months = int(input("Enter the number of months you plan to repay the mortgage: "))

    repayment = (rate * present_value) / (1 - (1 + rate)**(-months))
    print("Monthly repayment: ""£", repayment)

else:
    print("Invalid choice. Please enter 'investment' or 'mortgage' again.")


#------Clean--------------------------------------------------------------