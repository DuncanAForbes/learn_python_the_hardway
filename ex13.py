name = raw_input("What is  your name? ")
age = raw_input("What is  your age? ")

print "Your name is %r and you are %r years old." % (
	name, age)


from sys import argv

script, first, second, third = argv 


print "The script is called:", script
print "Your first variable is", first
print "You second variable is:", second
print "Your third variable is:", third
