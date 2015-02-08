from sys import argv

script, input_file = argv

def print_all(f):
	print f.read() # function read file

def rewind(f):
	f.seek(0) # seek sets he files current position

def print_a_line(line_count, f):
	print line_count, f.readline() # 'f.readline()' reads a single line from the file

current_file = open(input_file) # open()returns a file or object

print "First let's print the whole file:\n" # \n represents single line

print_all(current_file) # prints current file

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Lets print three lines:"
# prints current files lines 1, 2 and 3
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)