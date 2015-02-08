# 'def' defines the function 'cheese_and_crackers' which the defines to arguments ('cheese_count' and ' boxes_of_crackers')
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count # prints total number of cheeses
	print "You have %d boxes of crackers!" % boxes_of_crackers # prints total number of boxes of crackers
	print "Man that's enough for a party!"
	print "Geta bankets.\n"


print "We can just give the function number directly:"
cheese_and_crackers(20, 30) #

print "OR, we can use vairables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50


cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can we even do maths inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 