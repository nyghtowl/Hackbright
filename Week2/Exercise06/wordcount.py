from sys import argv

scirpt, filename1 = argv

file_container = open(filename1).read()

string_lower = file_container.lower()
list_split = string_lower.split()



word_dict = {}


# print a
for word in list_split:
	word = word.strip('-_,:.";?')
	word_dict[word] = word_dict.get(word, 0) + 1 
#	print a.count(i)


for key, value in word_dict.iteritems():
	print key, value

#print wordDict
