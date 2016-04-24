import csv
import re,sys
f = open('target.txt', 'w')
#print "Hello"
with open('new.csv', 'rb') as csvfile:
	filereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in filereader:
		#print row
		rowString =  ' '.join(row)
		#remove quotes from string
		rowString = rowString.replace('"', '')
		rowString = rowString.replace(',', '')
		#(?=.*[A-Z])(?=.*[0-9])
		for word in rowString.split(' '):
			if re.match(r'(?=.*[A-Z])(?=.*[0-9])', word):
				f.write(word)
				f.write('\n')
