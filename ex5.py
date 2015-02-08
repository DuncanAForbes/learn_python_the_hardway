name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
kilos = weight * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#This prints the above data
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d ounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth 
print "This is my weight in kilos %s." % kilos 

# this line is trickym try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)