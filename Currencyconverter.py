from sys import argv
prompt = '> '
print "Please select a currency"
currency = ['USD', 'GEL','EUR','GBP','INR','AUD','RUB','TRY' ]
print currency
user_input1 = raw_input(prompt)



if user_input1 == 'USD':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "GEL":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 2.469)
		print "Converted Enjoy: %d" % final
	if user_input2 == "EUR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.908)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GBP":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.702)
		print "Converted Enjoy: %d" % final
	if user_input2 == "INR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 66.98)
		print "Converted Enjoy: %d" % final
	if user_input2 == "AUD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.344)
		print "Converted Enjoy: %d" % final
	if user_input2 == "RUB":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 71.87)
		print "Converted Enjoy: %d" % final
	if user_input2 == "TRY":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 2.90)
		print "Converted Enjoy: %d" % final
if user_input1 == 'GEL':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "USD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.404)
		print "Converted Enjoy: %d" % final
	if user_input2 == "EUR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.367)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GBP":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.284)
		print "Converted Enjoy: %d" % final
	if user_input2 == "INR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 27.123)
		print "Converted Enjoy: %d" % final
	if user_input2 == "AUD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.544)
		print "Converted Enjoy: %d" % final
	if user_input2 == "RUB":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 29.101)
		print "Converted Enjoy: %d" % final
	if user_input2 == "TRY":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.176)
		print "Converted Enjoy: %d" % final
if user_input1 == 'EUR':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "USD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.101)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GEL":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 2.719)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GBP":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.774)
		print "Converted Enjoy: %d" % final
	if user_input2 == "INR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 73.765)
		print "Converted Enjoy: %d" % final
	if user_input2 == "AUD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.480)
		print "Converted Enjoy: %d" % final
	if user_input2 == "RUB":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 79.146)
		print "Converted Enjoy: %d" % final
	if user_input2 == "TRY":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 3.198)
		print "Converted Enjoy: %d" % final
if user_input1 == 'GBP':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "USD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.422)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GEL":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 3.513)
		print "Converted Enjoy: %d" % final
	if user_input2 == "EUR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.292)
		print "Converted Enjoy: %d" % final
	if user_input2 == "INR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 95.305)
		print "Converted Enjoy: %d" % final
	if user_input2 == "AUD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.912)
		print "Converted Enjoy: %d" % final
	if user_input2 == "RUB":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 102.257)
		print "Converted Enjoy: %d" % final
	if user_input2 == "TRY":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 4.132)
		print "Converted Enjoy: %d" % final
if user_input1 == 'INR':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "USD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.0149)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GEL":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.0368)
		print "Converted Enjoy: %d" % final
	if user_input2 == "EUR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.0135)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GBP":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.0104)
		print "Converted Enjoy: %d" % final
	if user_input2 == "AUD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.02007)
		print "Converted Enjoy: %d" % final
	if user_input2 == "RUB":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.0729)
		print "Converted Enjoy: %d" % final
	if user_input2 == "TRY":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.04336)
		print "Converted Enjoy: %d" % final
if user_input1 == 'AUD':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "USD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.74377)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GEL":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 1.8369)
		print "Converted Enjoy: %d" % final
	if user_input2 == "EUR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.675)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GBP":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.5227)
		print "Converted Enjoy: %d" % final
	if user_input2 == "INR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 49.8244)
		print "Converted Enjoy: %d" % final
	if user_input2 == "RUB":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 53.4585)
		print "Converted Enjoy: %d" % final
	if user_input2 == "TRY":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 2.16054)
		print "Converted Enjoy: %d" % final
if user_input1 == 'RUB':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "USD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.01391)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GEL":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.03436)
		print "Converted Enjoy: %d" % final
	if user_input2 == "EUR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.01263)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GBP":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.00978)
		print "Converted Enjoy: %d" % final
	if user_input2 == "INR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.93202)
		print "Converted Enjoy: %d" % final
	if user_input2 == "AUD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.01871)
		print "Converted Enjoy: %d" % final
	if user_input2 == "TRY":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.04042)
		print "Converted Enjoy: %d" % final
if user_input1 == 'TRY':
	print "Please select a currency to convert %r into ..." % user_input1
	currency.remove(user_input1)
	print currency
	user_input2 = raw_input(prompt)
	if user_input2 == "USD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.34425)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GEL":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.85023)
		print "Converted Enjoy: %d" % final
	if user_input2 == "EUR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.31263)
		print "Converted Enjoy: %d" % final
	if user_input2 == "GBP":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.24197)
		print "Converted Enjoy: %d" % final
	if user_input2 == "INR":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 23.0611)
		print "Converted Enjoy: %d" % final
	if user_input2 == "AUD":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 0.46285)
		print "Converted Enjoy: %d" % final
	if user_input2 == "RUB":
		print "Please enter how much %r you want to convert into %r " % (user_input1, user_input2)
		money = float(raw_input(prompt))
		final = (money * 24.7431)
		print "Converted Enjoy: %d" % fina