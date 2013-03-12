# Exercise 06
'''
Go through a file and count the number of words in the file
'''

from sys import argv 

scirpt, filename1 = argv # pull filename off command line

file_container = open(filename1).read() # open and read file to string

# Converted to lowercase, replaced dashes with space and split into a list
string_lower = file_container.lower() 
list_replace = string_lower.replace('-', ' ')
list_split = list_replace.split() # this version removes whitespace

# sets an empty dictionary
word_dict = {}


# loop through list, strip out end characters and assign to dictionary
for word in list_split:
	word = word.strip("'-_,:.\"*;?!)")
	# get checks if it exists and then assigns the key and adds value
	word_dict[word] = word_dict.get(word, 0) + 1  

# Following provides the user to choose print out option
print "Enter a if you want to sort by alphabet and 1 if by number: ",
sort_option = raw_input("> ")

# the dictionay is printed either sorted by key or by value and if neither of those then the raw dictionary
if sort_option == 'a':
	for key in sorted(word_dict.iterkeys()):
		print key, word_dict[key]
elif sort_option == '1':
	for key, value in sorted(word_dict.iteritems(), key=lambda (k,v): (v,k)):
		print key, value
else: 
	print word_dict