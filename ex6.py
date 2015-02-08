x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
#This prints out 'x' and 'y' into a sentance. 
print "I said: %r." %x
print  "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# When printing this turns the above 'hilarious' variable into a sentance joined with 'joke_evaluation'.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e