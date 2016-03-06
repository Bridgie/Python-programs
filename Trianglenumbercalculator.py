from sys import argv

prompt = '> ' 

print "Please input a number"
user_input1 = int(raw_input(prompt))

if user_input1 < 1:
	print "Please try again and input a number more than 1"
else:
	final = (user_input1 * (user_input1 + 1)) / 2
print final