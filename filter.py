from string import strip

def main():
	print '''\nString splits text files, then arranges and combines
them according to a selected column from each text file.'''
	print 'How many files?'
	x = raw_input('>> ')
	# handles queue of 1 separately
	if int(x) == 1:
		fileopened, spoint, col = filename()
		splittext = filterer(fileopened, spoint)
#		print 'First 3 lines:'
#		print splittext[:3]
	grand, colgrand = [], []
	# processes each file in turn
	# should change this to allow input of all parameters first
	for i in range(int(x)):
		fileopened, spoint, col = filename()
		splittext = filterer(fileopened, spoint)
		grand.append(splittext)
		colgrand.append(int(col))
	output = []
	for text in range(len(grand)):
		if text+1 < len(grand):
			output = combiner(grand[text], grand[text+1], colgrand[text], colgrand[text+1])
#	print 'First 3 lines of each text:'
#	for j in grand:
#		print j[:3]
#	print 'Result:'
#	print output
	# nicer output
	for k in output:		
		outputstring = ''
		for l in range(len(k)):
			if l < len(k)-1:
				outputstring += k[l] + ' | '
			else: outputstring += k[l]
		print outputstring




def filename():
	print 'Enter filename.'
	fname = raw_input('>> ')
	print 'Enter characters to be used as string split points.'
	spoint = raw_input('>> ')
	print 'Which column to arrange by?'
	col = raw_input('>> ')
	f = open(fname, 'r')
	return f, spoint, col


# could have used string.split() instead
def filterer(text, spoint):
	slist, split = [], []
	for s in spoint:
		slist.append(s)
	for line in text:
		# removes \r and \n
		linealone = strip(line, '\n')
		linealone = strip(linealone, '\r')
		linesplit = []
		a, b = 0, 0
		# splits the text according to string split points
		for char in range(len(linealone)):
			if linealone[char] in slist:
				b = char
				if linealone[a:b]:
					linesplit.append(linealone[a:b])
				a = b + 1
			elif char == len(linealone)-1:
				linesplit.append(linealone[a:])
		split.append(linesplit)
	return split


# here we consider just the column directly after the provided one
# and assume that col < len(text)
def combiner(text1, text2, col1, col2):
	tot = []
	for i in range(len(text1)):
		x = []
		x.append(text1[i][col1-1])
		x.append(text1[i][col1])
		for j in range(len(text2)):
			if text2[j][col2-1] == text1[i][col1-1]:
				x.append(text2[j][col2])
		tot.append(x)
	return tot



main()