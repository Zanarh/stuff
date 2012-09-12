# Build 12.09.2012

# This program splits each line of a given text file according to
# a given list of characters, i.e. the text is split at each
# character, if present within the text.

# Testing the program with the following files:
# 	testing.tbl, testing.ext
# and with the following inputs:
# 	>> 2
# 	>> testing.tbl
# 	>> |
# 	>> 5
#	>> 6
# 	>> testing.ext
# 	>> |
# 	>> 1
#	>> 2

# The result should be:
# 0001 | Last Trade/Last Price | Last price for the security. Field updates in realtime.
# 0002 | Bid Price | Current bid price in the market.
# 0003 | Ask Price | Current ask price in the market.

# Requirements:
# - Each line in a text file has the exact same formatting
# - Column to be used to identify lines to be combined has to be specified
# - Columns to be included in the final output has to be specified

# Inputs:
# - How many files to combine?
# - For each of the files:
# 	- What is the filename (e.g. textfile.txt)?
# 	- What are the characters to split the file by (e.g. \|,)?
# 	- Which one is the identifying column?
#	- Which columns are to be included in the output?

# To be fixed:
# - Breaks if none of the identifiers match
# - Identifying column should be given only for first file;
#		should be found automatically for subsequent files
# - Works well only with text files of equal number of lines
#		i.e. does not handle repeated identifiers
# - Add save output to file functionality at the end
# - Allow supression/input for column borders in output
# - Add choice of split/combine at beginning


from string import strip, split

def main():
	print '''\nString splits text files, then arranges and combines
them according to a selected column from each text file.'''
	print 'How many files?'
	x = raw_input('>> ')
	# handles queue of 1 separately
	# if int(x) == 1:
	# 	fileopened, spoint, col = filename()
	# 	splittext = filterer(fileopened, spoint)
#		print 'First 3 lines:'
#		print splittext[:3]
	# using lists here instead of dictionaries
	# bad idea?
	grand, colid, colgrand = [], [], []
	# processes each file in turn
	# should change this to allow input of all parameters first
	for i in range(int(x)):
		# idcol is an integer
		# col here is a string/list
		filetobeopened, spoint, idcol, col = filename()
		fileopened = open(filetobeopened, 'r')
		splittext = filterer(fileopened, spoint)
		grand.append(splittext)
		colid.append(idcol)
		colgrand.append(col)
	# could show sample output here		
	output = []
	for text in range(len(grand)):
		if text < len(grand):
			output = cmbnr(output, grand[text], colid[text], colgrand[text])
			# output = combiner(grand[text], grand[text+1], colgrand[text], colgrand[text+1])
#	print 'First 3 lines of each text:'
#	for j in grand:
#		print j[:3]
#	print 'Result:'
#	print output
	# nicer output
	print 'Result:'
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
	f = open(fname, 'r')
	fline1 = f.readline()
	fline1 = strip(fline1, '\n')
	fline1 = strip(fline1, '\r')
	print 'The text looks like:'
	print fline1
	print 'Enter characters to be used as string split points.'
	spoint = raw_input('>> ')
	splittxt = flt(fline1, spoint)
	# adds on column number indicators
	output = ''
	for i in range(1, len(splittxt)+1):
		output += str(i) + ':' + splittxt[i-1] + '|'
		if i < len(splittxt):
			output += '  '
	print 'The split text looks like:'
	print output
	print 'Which is the identifying column?'
	idcol = raw_input('>> ')
	print 'Which columns to include?'
	col = raw_input('>> ')
	collist = col.split(',')
	return fname, spoint, int(idcol), collist


# could have used string.split() instead?
def filterer(text, spoint):
	slist, split = [], []
	for s in spoint:
		slist.append(s)
	for line in text:
		# removes \r and \n
		linealone = strip(line, '\n')
		linealone = strip(linealone, '\r')
		linesplit = []	# for containing the split text
		a, b = 0, 0	# for counting the start and end points of a string
		# splits the text according to string split points
		for char in range(len(linealone)):
			if linealone[char] in slist:
				b = char	# end point of string
				if linealone[a:b]:	# ignores empty strings
					linesplit.append(linealone[a:b])
				a = b + 1	# new point in the text for string consideration
			elif char == len(linealone)-1:	# if no string point remains, closes string at end
				linesplit.append(linealone[a:])
		split.append(linesplit)
	return split

# for use with filename()
# to be integrated with filterer()
def flt(text, spoint):
	slist = []
	for s in spoint:
		slist.append(s)
	linesplit = []
	a, b = 0, 0
	for char in range(len(text)):
		if text[char] in slist:
			b = char	# end point of string
			if text[a:b]:	# ignores empty strings
				linesplit.append(text[a:b])
			a = b + 1	# new point in the text for string consideration
		elif char == len(text)-1:	# if no string point remains, closes string at end
			linesplit.append(text[a:])
	return linesplit


# here we consider just the column directly after the provided one
# and assume that col < len(text)
# also assume that each line has the same format
# rewrite below
# def combiner(text1, text2, colid1, colid2, col1, cold2):
# 	tot = []
# 	for i in range(len(text1)):
# 		x = []
# 		# have to adjust the col values
# 		x.append(text1[i][colid1-1])
# 		for cols in col1:
# 			x.append(text1[i][int(cols)1])
# 		for j in range(len(text2)):
# 			if text2[j][colid2-1] == text1[i][colid1-1]:
# 				for sloc in cold2:
# 					x.append(text2[j][int(sloc)-1])
# 		tot.append(x)
# 	return tot


# use this instead
def cmbnr(tot, text, colid, cols):
	# initiates the output with identifying column elements
	if tot == []:
		for i in range(len(text)):
			x = []
			x.append(text[i][colid-1])
			if isinstance(cols, list):
				for j in cols:
					x.append(text[i][int(j)-1])
			else:
				x.append(text[i][int(cols)-1])
			tot.append(x)
	# have to allow for handling of repeated identifiers
	else:
		for k in range(len(tot)):
			for i in range(len(text)):
				x = []
				if text[i][colid-1] == tot[k][0]:
					for sloc in cols:
						tot[k].append(text[i][int(sloc)-1])
	return tot


main()