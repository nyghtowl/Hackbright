import random

def topBot(x, step):
	i = 0
	numbers = []

	for i in range(x):
		print "At the top i is %d" % i
		numbers.append(i)

		i += step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

y = random.randint(0,20)
topBot(5, 2)

'''
def topBot(x, step):
	i = 0
	numbers = []

	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)

		i += step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

y = random.randint(0,20)
topBot(y, 2)
'''