answer = input("Could you like to hear a joke? ")


# this is a way to shorten the if statment.
# i have further shortened it with lowering the answer before checkng it

correct_ans = ["yes","y"]
wrong_ans = ["no","n"]

if answer.lower() in correct_ans:
	print("Life is a joke all the time..!!!")

elif answer.lower() in wrong_ans:
	print("No worries")

else:
	print("please make a choice of either Yes or No")


for num in range(1,11):
	print(num * num)
