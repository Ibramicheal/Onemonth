# creating a function that uppercases and reverses the input.

def up_and_reverse(string):
	result = string.upper()[::-1]
	return result


print(up_and_reverse("you are one crasy fool!"))	