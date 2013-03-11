# Project X is Hackbright Week1 project 
''' Create 26 directories in the current directory, one for each
letter of the alphabet. 

Loop through all the files in the original_files directory, and
organize each of those files into the directory that their name
starts with.

''' 

import os
import shutil
import string

origin = os.listdir('./files/') 

# print os.path.exists('./files') 
# print os.getcwd()

alph = string.letters[0:26]
print alph
for let in alph:
	newDir = './'+ let + '/'
	os.mkdir(newDir)
	for f in origin:
		if f.startswith(let):
			shutil.move('./files/' + f,newDir)
		# os.chdir('./files')



