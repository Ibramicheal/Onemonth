# this calculator is going to determines the perecentage of a tip.
# gets bills from custome
bill = float(input("What is your bill? ").replace("£"," "))
print("bill")
# calculates the options for tips.
tip_one = 0.15 * bill
tip_two = 0.18 * bill
tip_three = 0.20  * bill
# prints out the options avaible.
print(f"You bill is {bill} and you have 3 options for a tip, option 1 is {tip_one:.2f}, option 2 is {tip_two:.2f}, option 3 is {tip_three:.2f}. ")
option_for_tip = float(input("Which option would you like to choice? "))
print(f"Thank you for choicing option {option_for_tip:.0f} .Please come agian.")
