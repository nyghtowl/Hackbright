#imports argv function from python file sys
#this is entirely equivalent to just "import sys" and then later using "sys.argv" below instead of just "argv"

from sys import argv

# applies two values to argv from the command line
script, filename = argv

# txt variable opens the filename that has been passed from argv
txt = open(filename)

# following prints the name of the file and then reads and prints the contents of the file
print "Here's your file %r:" % filename
print txt.read()

txt.close()

# This is the same as the above except it has an extra step to input the filename
# following asks for the filename again which is assigned to the variable file_again
print "Type the filename again:"
file_again = raw_input("> ")

# txt_again is a new variable that opens files_again
txt_again = open(file_again)

# read function runs on txt_again to read and print the content
print txt_again.read()

txt_again.close()