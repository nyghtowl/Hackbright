# this is the function that is being used below
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print " You have %d cheeses!" % cheese_count
	print " You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# example of passing numbers directly to the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# example of passing variables to the function that reference numbers
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# example of doing math in the function call to pass values
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# example of using variables and numbers and math operators to pass values
# to the function 
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)