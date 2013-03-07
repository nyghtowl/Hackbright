import random

prompt = '> '
print "What's your name?"
name = raw_input (prompt)

print "Hello %s!" % name 

print "Let's play a game! Pick any number between 1 and 20." 

i = random.randint(1,20)

guess = 0 

while True:
	guess = guess + 1
	number = int(raw_input(prompt))

 	
 	if number < i:
		print "The number is too low. Try again."
	
	elif number > i:
		print "The number is too high. Try again."
	
	else:
		print "You guessed it! Great job, %s. You found my number in %d tries." % (name, guess)
		break
	