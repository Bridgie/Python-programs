from sys import argv

	
prompt  = '> '

print "Hello please enter your height in Meters"
height = float(raw_input(prompt))
height = height * height

#print height

print "Please enter your weight in Kilograms"
weight = int(raw_input(prompt))

final = float(weight / height)
print "Your BMI is %d" % final
print "Healthy BMI range is between 19 and 25 "
if final < 19:
	print "Your BMI is unhealthy: too skinny"
elif final > 25:
	print "Your BMI is unhealthy: too fat"
else:
	print "Your BMI is Healthy"