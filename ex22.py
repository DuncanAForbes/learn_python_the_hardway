#  I'm an (ochra) used for commenting your code

() # Parathensis



a = 1 + 0 # plus

print "%s" % a 

b = 1 - 2 # minus

print "%s" % b

c = 2 * 2 # asterisk also Mulitply

print "%s" % c

d = 3 % 3 # percent also used to link modifiers '%r', '%a', '%s', '%n', '%d' and also used to connect function or variable to a print output 'print "Hello %s" % hello_you'.

print "%s" % d

e = 4 < 5 # less-than

print "%s" % e

f = 5 > 6 # more-than

print "%s" % f

if (7 <= 8):
	print "7 is less than 8"
else:
	print "7 is more than 8"
 # less-than-equal
if (2 >= 3): # more-than-equal
	print "2 is great than 3"
else:
	print "2 is not greater than 3"

print "hello" # Prints a functions (commmands) output or input

print """
Hello World....
Hello Galaxies....
Hello Universies....
""" # Prints ' print """xxx""" 'sentences

print "%f" # character 'float'
print "%d" # character 'digit'
print "%s" # character 'string' (only use this) otherwise use the below for 'debugging'
print "%r" # character 'representation' (used for debugging) and givesraw programmers view. 

print "\* test" # slash asterisk creates a 'double quote'
print "\'" # slash coma creates a 'single quote'
print "\a" # ASCII Bell (BEL) - '\a'
raw_input('\f') # ASCII formfeed (ff) - '\f'
print "\n " # character name in database (unicode only) also '\n' is for lines
example = '\u00bfHabla' # character with 32 bit HEX Value 'xxxxxxxx' (unicode only)
print "\v test" # ASCII Vertical tab (VT)
print "\000 test" # Character with octal value
print "\x00 test" #character with hex value hh




#Ask a quesiton example:


print "How old are you?"
x = raw_input()

print "Where do you live?"

y = raw_input()

print "You are %r years old and you live in %r. Awesome." % (x, y)





string_one = (1, 2, 3, 4) # simple string method example 1.

print "%s"	% list(string_one) # 'list' returns a list

string_two = ("one","two","three","four") # simple string method example 2.

print "%r" % list(string_two)


#from sys  # location of module / 'sys' is the module library

#import argv  # 'argv' Argument Variable module / 'import' imports a module



#Basic program that prints an argument variable (argv)

from sys import argv

script, first = argv

print "This is the name of your script %s" % script
print "This is your first variable %s." % first




#Argument Variable (argv) prompt example

from sys import argv

script, user_name = argv

prompt = '>'

print "Hello %r, welcome to the script %r" % (user_name, script)
print "We are now going to ask you some questions."
print "How old are you %r? " % user_name
age = raw_input(prompt)

print "Do you like me %r? " % user_name
like = raw_input(prompt)

print "What sport do you love?"
sport = raw_input(prompt)


print "%s you are %r years old. You answered %s to liking me. And you love %s." % (user_name, age, like, sport)
 


#read() # reads at most size bytes from file
#open() # returns a file object
#close() # closes file object like / file -> save in a text editor


#Example: Reading Files

from sys import argv

script, file_name = argv

txt = open(file_name)

print "This is your %r file."  % file_name
print txt.read()

print "Type your file name again."
file_again = raw_input('> ')

txt_again = open(file_again)

print txt_again.read()


#write('stuff') # write('stuff') writes "stuff" to a file

# target = open('w') # opens file in write mode. Also truncates file
# target = open('r') # opens file in read mode.
# target = open('a') # appends file

# Modifers of 'a', 'r' and 'm'

print " '+' is the most important modifer at this time 'a+','r+','m+' "
print """
An example of a modifer is.
	\* target = open('w+')
"""

# exists() # This command (Function) returns true if file exists
# len() # 

def print_all(f): # 'def' defines a function. The 'f' in print_all is just a variable in all other functions. Except it is a (file).
	print f. read()

def rewind(f):
	f.seek(0) # everytime you do f.seek you are moving to the start of the file. The code seek(0) moves the file to the 0 bytes(first byte)

def print_a_line(line_count, f):
	print line_count, f.readline() # inside 'readline()' is the code that scans eavh byte of the file until it finds a '\n' character, then stops reading the file to return what it found so far. The 'f' is responisble for maint the current position in the file after each readline() call, so that it wil keep reaadind each line.


# current_line = 1
# print_a_line(current_line, current_file)  

# current_line += 1
# print_a_line(current_line, current_file) # '+=' means the same as 'x = x = y'


# x.copy() # return a shallow copy of x


def print_two(*args):
	arg1, arg2 = args
	print "Arg1: %r, Arg2: %r " % (arg1, arg2)  # '*args' tells Python to take all the arguments to the function and then put them in args as a lit. Like 'argv' (argument variables) but for functions.


def add(a, b):
	print "ADD %d + %d" % (a, b)
	return a + b

something = add(77, 77)

print "Something %d " % (something) # Using functions to do simple maths








