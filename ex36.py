from sys import exit


def forest():
	print "The forest is dark. You feel like you are being watched." 
	print "You are alone. A chill descends down your spine."
	print "You feel something pick you up."
	print "You are flung into a tree."
	print "A shadow or shadows keep appearing from no where."
	print "They make a clanking sound."
	print "You try to jump out of the tree"
	print "You realise upon falling. It is a massive cat fight."
	print "You land on a giant spike."
	print "Your head splits in two."
	dead_one()





def castle_tower():
	print "Ok. So your in the tower. Its bleak up here. Pretty high to."
	print "Most cats don't come here. Actually most die here."
	print "You hear a faint question from a light in a dark corner."
	print "You ask who it is. The light responds with. It dosen't matter."
	print "Answer this question and you may leave forever. Or else you will be hear for enternity."
	print "Who started the Cubism Movement?"
	print "\n A: Picasso B: Braque"

	choice = raw_input("> ")

	if choice == "A":
		print "That is wrong. The answer is Braque. You shall die alone in this bleak cold foodless tower."
		exit(0)
	elif choice == "B":
		print "That is correct. You may now go home and sleep."
		exit(0)




def stream():
	print "You enter the magical land of the stream."
	print "You see lots of lovely birds dipping and diving all over the place."
	print "Butterflies and dragonflies all over the place."
	print "What do you do?" 
	print "A. Guess the nearest total number of butterflies there are."
	print "B. Try and catch birds."
	print "C. Splash about in the water."

	choice = raw_input("> ")
	butterflies_x = int(choice)

	if butterflies_x < 50:
		print "You were almost correct. But not quite. There are 150."
		print "The sour truth and trick in the game is this."
		print "You will now spend eternity in the castle tower. Ouch."
		print "To the tower you go."
		castle_tower()

	if butterflies_x > 50:
		print "Well done. You were very close to the number of butterflies. You win."
		exit(0)





def clock_tower():
	print "By the time you reach the clock_tower the sun is going down."
	print "You decide to watch the sun set."
	print "There are crows cawwing about."
	print "You hear puring and hissing."
	print "There is grey cat with blue eyes."
	print "You wonder over. He looks at you. Startled. Staring into your sole."
	print "And who might you be? the cat with the blue eyes says."

	name = raw_input("> ")

	print "Hello %s. What are you doing here?" % name
	print "This my spot."

	print "\n How do you respond."
	print "1. I've never seen you before. I come here all time. How is it your spot?"
	print "2. I live nearby. I like seeing the sunset from here. It relaxes me."
	print "3. I think I shall be leaving. I didn't mean to disturb you."

	print "\nType the question number to answer."

	what = raw_input("> ")

	if what == "1":
		dead("The blue eyed cat pounces on you. This the mother of all cat fights.")
	elif what == "2":
		print "As do I to. The blue eyed cat says. How about we watch the sunset together?"
		print "Answer: Yes I'd love to / No thank you?"

		sunset = ("> ")

		if sunset == "Yes I'd love to":
			sleep("You now stare into nothingness and chat with the blue eye cat. Until dozing off.")
		elif sunset == "No thank you":
			print "Very well then the blue eyed cat responds."
			home("Decide to head home")
	elif what == "3":
		forest("You decide to head into the forest.")





def the_wall():
	print """
	"Who are you?" the black tabby cat says.
	"""
	name = raw_input("> ")

	print "Hello %s. That is a lovely name." % name
	print "My name is Rapheal."

	print "Ask the tabby a question?"
	print "1. Rapheal where do you come from?"
	print "2. Do you fancy going to the stream?"
	print "3. How about we go to the clock tower?"
	print "\nType the question number to answer."

	choice = raw_input("> ")

	if choice == "1":
		print "I come from a faraway land. Not known by many..."
		sleep("You doze off.")
	elif choice == "2":
		print "Yes I'd love to."
		stream()
	elif choice == "3":
		print """
		I was there yesterday thank you.
		It is quite fun. But I don't fancy it today.
		"""
		clock_tower("You head to the clock tower alone.")




def the_house():
	print """
	You stroll into the kitchen of the house.
	You are picked up by one of your owners.
	Your owner starts cuddling you.
	Do you 1. Try to jump out of their arms? and 
	runaway to the stream. 2. Scratch them. 
	Or 3. Snooze."""
	print "\nType the number to your answer."

	choice = raw_input("> ")

	if choice == "1":
		stream("After struggling for a minute or so. You squeeze your way out of the arms of your owner. And runaway to the stream.")
	elif choice == "2":
		dead_two("You scratch your owner. They are next to stove cooking. You fall into the hot broth. And die.")


def the_garden():
	print "You stroll into the garden. There is a butterfly."
	print "And a cat on the wall."
	print "Do you say hello to the cat on the wall? or chase the butterfly?"

	choice = raw_input("> ")

	if choice == "Chase Butterly":
		forest()
	elif choice == "Say hello to the cat":
		the_wall()
	else:
		sleep("You decide to snooze.")


def dead_two():
	print "Well that was a bad decision."
	print "Yes you are really dead!"
	exit(0)


def dead_one():
	print "You lost to that mighty cat fight."
	print "Yes you are really dead!"
	exit(0)


def sleep(why):
	print "You are now dreaming of cows..."
	exit(0)


def start():
	print "You are outside in the sunshine. Purring." 
	print "Yes you are a cat."
	print "You are pondering what to do with your day."
	print "There is a forest nearby. A castle. A stream. A clock tower."
	print "A wall. Your house and the garden."
	print "Where do you wish to explore?"

	choice = raw_input("> ")

	if choice == "the house":
		the_house()
	elif choice == "the garden":
		the_garden()
	elif choice == "the stream":
		stream()
	elif choice == "the castle":
		castle_tower()
	elif choice == "the forest":
		forest()
	elif choice == "the wall":
		the_wall()
	elif choice == "clock_tower":
		clock_tower()
	else:
		sleep("You decide to doze off in the sun...")


start()
