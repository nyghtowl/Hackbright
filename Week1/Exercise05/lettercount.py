from sys import argv
import string

script, filename = argv #on the command line, user should enter twain.txt as an argument

book = open(filename).read()
bookLower = book.lower()

ord_list = [0] * 26

for i in bookLower: #go through each letter in the text
	charNum = ord(i) - 97 #get the ordinal number of that letter. Subtract 97 to get its distance from a
	if charNum >=0 and charNum <= 26:
		ord_list[charNum] += 1 #add one to the tally in that index location
	else:
		continue


for x in range(len(ord_list)):
	print ord_list[x]



'''
newList = list(bookLower)
print newList[20]

alphabet_list = string.lowercase

#make alphabetical list
#go through the alphabet...

for i in alphabet_list:
	print i,  `  newList.count(i) 

#for i in range(len(book)):


#	uniCapture = ord(book[i])
#	book.count(uniCapture, 0, len(book))


#string.lowercase()
'''

