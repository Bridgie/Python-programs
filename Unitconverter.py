from sys import argv

prompt = '> '

print "Please choose an unit..."

unit = ['Weight','Length','Volume','Area', 'Speed', 'Temperature']

weight = ['Kilotonne','Tonne','Kilonewton','Centner','Kilogram','Newton','Carat','Gram','Milligram',]
length = []
volume = []
area = []
speed = []
temperature = []

print unit

user_input1 = raw_input(prompt).title()

if user_input1 == "Weight":
	print "Please input which unit you want converted"
	print weight
	user_input2 = raw_input(prompt).title()
	if user_input2 == "Kilotonne":
		print "Please enter which unit to convert %r into....:" % user_input2
		weight.remove(user_input2)
		print weight
		user_input3 = raw_input(prompt).title()
		if user_input3 == "Tonne":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 1000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Kilonewton":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 9806.65)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Centner":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 10000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Kilogram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 1000000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Newton":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 9806650.02864)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Carat":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 5000000000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Gram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 999999999.9999999)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "MilliGram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 1000000000000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_inpufloat)


	if user_input2 == "Tonne":
		print "Please enter which unit to convert %r into....:" % user_input2
		weight.remove(user_input2)
		print weight
		user_input3 = raw_input(prompt).title()
		if user_input3 == "Kilotonne":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 0.001)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Kilonewton":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 9.964016384)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Centner":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 20)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Kilogram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 1016.0469088)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Newton":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 8896.4432)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Carat":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 5080234.544)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Gram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 1016046.9088)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Milligram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 907184740)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)			

	if user_input2 == "Kilonewton":
		print "Please enter which unit to convert %r into....:" % user_input2
		weight.remove(user_input2)
		print weight
		user_input3 = raw_input(prompt).title()

		print "Please enter how much you want to convert"
		user_input4 = float(raw_input(prompt))
		final = float(user_input4 * 0.00010197162099998804)
		print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Tonne":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 0.10036113501930059)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Centner":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 2.03943242)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Kilogram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 101.971621)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Newton":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 1000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Carat":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 509858.105)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Gram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 101971.621)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Milligram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 101971621)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)						

	if user_input2 == "Centner":
		print "Please enter which unit to convert %r into....:" % user_input2
		weight.remove(user_input2)
		print weight
		user_input3 = raw_input(prompt).title()
		if user_input3 == "Kilotonne":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 0.00005)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Tonne":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 0.05)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Kilonewton":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 0.490332501432)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Kilogram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 50)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Newton":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 490.332501432)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Carat":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 250000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Gram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 50000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)
		if user_input3 == "Milligram":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 50000000)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)								
	if user_input2 == "Kilogram":
		print "Please enter which unit to convert %r into....:" % user_input2
		weight.remove(user_input2)
		print weight
		user_input3 = raw_input(prompt).title()
		if user_input3 == "Kilotonne":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 0.000001)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)		
		if user_input3 == "Tonne":
			print "Please enter how much you want to convert"
			user_input4 = float(raw_input(prompt))
			final = float(user_input4 * 0.001)
			print "%d %r is %d %r" % (user_input4,user_input2,final,user_input3)	