cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#The below variable collects the variables 'cars' and 'drivers' and minuses cars with drivers.
cars_not_driven = cars - drivers
cars_driven = drivers
#The below variable collects the variables 'cars' and 'drivers' and multiplies cars with drivers.
carpool_capacity = cars_driven * space_in_a_car
#The below variable collects the variables 'cars' and 'drivers' and divides cars with drivers.
average_passengers_per_car = passengers / cars_driven


#The below shall print out call variables into a sentence.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car." 