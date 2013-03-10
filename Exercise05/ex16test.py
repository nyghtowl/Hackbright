from sys import argv

script, filename = argv

#want to import test.txt

text = open(filename)
print text.read()