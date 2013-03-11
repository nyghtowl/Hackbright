from sys import argv
import string

scirpt, filename = argv

f = open(filename)

rest_list = {}

for line in f:
	strip_line = line.strip()
	split_line = strip_line.split(':')
	rest_list[split_line[0]] = rest_list.get(split_line[0], split_line[1])
for key in sorted(rest_list.iterkeys()):	
	print "Restaurant '%s' is rated at %s." % (key, rest_list[key])


f.close()

#alphabet = string.uppercase
# This does not work but what we worked through to get there
	#rest_list = dict(split_line[0] = split_line[1])
	#key = split_line[0]
	#rest_list[key] = rest_list.get(split_line[1],0)
'''
for letter in alphabet:
	if rest_list.startswith(letter)
'''
