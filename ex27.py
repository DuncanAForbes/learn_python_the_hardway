prompt = '> '

score = 0


 
def true_one():
	print "\nWell done. You are correct!"

def true_zero():
	print "\nIncorrect. Keep praticing. The answer is 'True'."

def false_one():
	print "\nWell done. You are correct!"


def false_zero():
	print "\nIncorrect. Keep praticing. The answer is 'True'."



def print_score(score):
	print "\nYour score is %d" % score




print "\nBoolean logic expressions. Answer these questions to memorise."
print "\nNOT. 'True' or 'False'?"


print "\nnot False?"
notfalse = raw_input(prompt)
if notfalse == "true":
		print true_one()
		score += 1
else:
	print true_zero()
		 	
			

print "\n not True?"
nottrue = raw_input(prompt)
if nottrue == "false":
	print false_one()
	score += 1
else:
	print true_zero()
		 	
		 	

print_score(score)



print "\nOR. 'True' or 'False'?"


print "\nTrue or False?"
true_or_false = raw_input(prompt)
if true_or_false == "true":
	print true_one()
	score += 1
else:
	print false_zero()
			

print "\nTrue or True?"
true_or_true = raw_input(prompt)
if true_or_true == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print "\nFalse or True?"
false_or_true = raw_input(prompt)
if false_or_true == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print "\nFalse or False?"
false_or_false = raw_input(prompt)
if false_or_false == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print_score(score)


print "\nAND. 'True' or 'False'?"

print "\nTrue and False?"
true_and_false = raw_input(prompt)
if true_and_false == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\nTrue and True?"
true_and_true = raw_input(prompt)
if true_and_false == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print "\nFalse and True?"
true_and_false = raw_input(prompt)
if true_and_false == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\nFalse and False?"
false_and_false = raw_input(prompt)
if false_and_false == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print_score(score)


print "\nNOT OR. 'True' or 'False'?"

print "\nnot(True or False). 'True' or 'False'?"
not_true_or_false = raw_input(prompt)
if not_true_or_false == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\nnot(True or True). 'True' or 'False'?"
not_true_or_true = raw_input(prompt)
if not_true_or_true == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\nnot(False or False). 'True' or 'False'?"
not_false_or_false = raw_input(prompt)
if not_false_or_false == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\nnot(True or False). 'True' or 'False'?"
not_false_or_false = raw_input(prompt)
if not_false_or_false == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print_score(score)


print "\nNOT OR. 'True' or 'False'?"


print "\nnot(True and False). 'True' or 'False'?"
not_true_and_false = raw_input(prompt)
if not_true_and_false == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print "\nnot(True and True). 'True' or 'False'?"
not_true_and_true = raw_input(prompt)
if not_true_and_true == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\nnot(False and True). 'True' or 'False'?"
not_false_and_true = raw_input(prompt)
if not_false_and_true == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print "\nnot(False and False). 'True' or 'False'?"
not_false_or_false = raw_input(prompt)
if not_false_or_false == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print_score(score)



print "\n != (not equal). 'True' or 'False'?"


print "\n 1 != 0 . 'True' or 'False'?"
one_not_equal_zero = raw_input(prompt)
if one_not_equal_zero == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print "\n 1 != 1 . 'True' or 'False'?"
one_not_equal_one = raw_input(prompt)
if one_not_equal_one == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\n 0 != 1 . 'True' or 'False'?"
zero_not_equal_one = raw_input(prompt)
if zero_not_equal_one == "true":
	print true_one()
	score += 1
else:
	print false_zero()

	print "\n 0 != 0 . 'True' or 'False'?"
zero_not_equal_zero = raw_input(prompt)
if zero_not_equal_zero == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print_score(score)



print "\n == (equal). 'True' or 'False'?"


print "\n 1 == 0 . 'True' or 'False'?"
one_equal_zero = raw_input(prompt)
if one_equal_zero == "false":
	print false_one()
	score += 1
else:
	print true_zero()


print "\n 1 == 1 . 'True' or 'False'?"
one_equal_one = raw_input(prompt)
if one_equal_one == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print "\n 0 == 1 . 'True' or 'False'?"
zero_equal_one = raw_input(prompt)
if zero_equal_one == "false":
	print false_one()
	score += 1
else:
	print true_zero()

	print "\n 0 == 0 . 'True' or 'False'?"
zero_equal_zero = raw_input(prompt)
if zero_equal_zero == "true":
	print true_one()
	score += 1
else:
	print false_zero()


print_score(score)
