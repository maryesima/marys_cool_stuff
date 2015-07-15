import random

num = random.randint(1,5)
guessestaken = 0
#guess = raw_input("Guess a number between 1 and 5: ")
#guess = int(guess)

while guessestaken <= 3:
	guess = raw_input("Guess a number between 1 and 5: ")
	guess = int(guess)
	guessestaken += 1
	if guessestaken == 3:
		print "You have used all 3 guesses."
		break
	if guess > num:
		print "Your guess is too high!"
	elif guess == num:
		print "Your guess is correct!"
		break	
	else:
		print "Your guess is too low."
