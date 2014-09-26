__author__ = 'shihchosen'
number = 23
running = True

while running:
    guess = int(input('Enter an integer: '))

    if guess == number:
        print('Congratulations, you guessed it.')
        running = False # this cause the while loop to stop
        print('(but you do not win any prizes!)')
    elif guess < number:
        print('No, it is alittle higher than that')
    else:
        print('No, it is a little lower than that')
else:
    print('The while loop is over.')
    # Do anything else you want to do here
print('Done')