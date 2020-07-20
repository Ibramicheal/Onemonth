# variables are the containers
# they hold vales ie number,letters etc

# this is the variable storing/holding ibrahim as a valve.
name = "Ibrahim" 

year_of_birth = 1987
curent_year = 2020

age = curent_year - year_of_birth

print("You are ", age, " old.")
# you can put a variable inside a print statement by separating with commas.

entry = 24.6997
vat = 20 % entry

price = vat + entry

print(f"You have to pay £{price:.2f}")
# . point lets pyhton know its a decimal
# 2 specifies how many places
# f makes it float