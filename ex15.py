from sys import argv
# the below are the script and variables to be used / ouput by the module 'argv'
script, filename = argv
# the below is the variable 'txt' which is to act as the calling function for the module 'open' create a "file object"
txt = open(filename)
# the below print function says the name of the file to the user
# the second print function below uses the module '.read' to read the 'txt' variable  to print the file that is to be opened
print "Here's your file %r:" % filename
print txt.read()
# the below print function ask the user to type the filename again.
# the 'file_again' variable allows a raw_input module function for the user to enter their file name into
print "Type the filename again:"
file_again = raw_input("> ")
# the below variable 'txt_again' with the below module 'open' with variable 'file_again' allows the user to enter their file name again 
txt_again = open(file_again)
# the below print function prints the above vairable 'txt_again'
print txt_again.read()