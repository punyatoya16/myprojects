
#computer number guessing game
import random
def guess(x):
	random_number=random.randint(1,x)

	guess = 0

	while (guess!=random_number):
		guess=int(input(f'uess a number between 1 n {x} '))
		
		if guess < random_number:
			print('too low')
		elif guess > random_number:
			print('too high')


	print(f"congrats number is {random_number}")


		
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)
# guess(10)




# from turtle import * 
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()
# logging in python
# import logging
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# dic={'prashant':87,'pratham':90,'fran':10,'raza':95}
# dic2={k:v for k,v in sorted(dic.items(),key=lambda x: x[1])}
# print(dic2)
# youtuber=" "
# print(f"subscribe to{youtuber}")