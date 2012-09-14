# Visualisation of the inclusion-exclusion principle in probability
# As shown here:
# http://en.wikipedia.org/wiki/Inclusion-exclusion_principle#In_probability


# Just to initiate
output = []


def probrest(a, n, count, counter, lister):
	counter += 1
	if counter <= count:
		for i in range(a, n+1):
			newlister = []
			for stuff in lister:
				newlister.append(stuff)
			newlister.append(i)
			probrest(i+1, n, count, counter, newlister)
	else:
		string = []
		for i in lister:
			string.append(str(i))
		global output
		output.append(string)


def probadd(n):
	outstring = '    = '
	for i in range(1, n+1):
		outstring += 'P(A' + str(i) + ')'
		if i != n:
			outstring += ' + '
	return outstring


def probu(n):
	outstring = 'P('
	for i in range(1, n+1):
		outstring += 'A' + str(i)
		if i != n:
			outstring += ' U '
		else: outstring += ')'
	return outstring


def issign(n):
	if n%2 == 0:
		return '-'
	else: return '+'


# Use this
def allprob(n):
	print probu(n)
	print probadd(n)
	for i in range(2, n+1):
		global output
		output = []
		probrest(1, n, i, 0, [])
		operator = issign(i)
		for j in output:
			outstring = '      ' + operator
			for k in range(len(j)):
				outstring += ' A' + j[k]
				if k != len(j)-1:
					outstring += ' &'
			print outstring


print "How many events?"
x = raw_input('>> ')
allprob(int(x))