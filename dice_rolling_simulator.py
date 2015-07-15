import random

min = 1
max = 6

roll_again = "yes"
        
while roll_again == "yes":
	print random.randint(min,max)
	print random.randint(min,max)
	print "Would you like to roll again?"
	roll_again = raw_input("Roll again? ")

