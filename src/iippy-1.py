# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

def new_game():
    range100()

def range100(): 
    global secret_num , n , mode
    mode = 1
    secret_num = random.randint(0, 99)
    print 'A positive integer from 0 to 99 has been chosen, guess!!!'
    n = n_calculator(100 , 0)

def range1000():     
    global secret_num , n , mode
    mode = 2
    secret_num = random.randint(0, 999)
    print 'A positive integer from 0 to 999 has been chosen, guess!!!'
    n = n_calculator(1000 , 0)
    
def n_calculator(high , low):
    n_c = int(math.ceil(math.log(high-low+1,2)))
    if n_c > 1:
        print 'You can try ' + str(n_c) + ' times.'
    elif n_c == 1:
        print 'You have just one chance!!!'
    elif n_c == 0:
        print 'This range does not work!!!'
        new_game()
    return n_c
        
def input_guess(guess):
    print 'Your guess is ' + guess +'.'
    try:
        guess = int(guess)
    except ValueError:
        print 'It has to be a positive integer. Try again...'
        return()
    global secret_num , n , mode
    if guess < secret_num:
        print 'Higher'
    elif guess > secret_num:
        print 'Lower'
    else:
        print 'Correct'
        print "Let's play the game one more time!"
        if mode == 1:
            range100()
        elif mode == 2:
            range1000()
    n = n-1
    if n > 1:
        print 'You can still try ' + str(n) + ' times.'
    elif n == 1:
        print 'Last chance!!!'         
    else:
        print 'You fail!!!'
        print "Let's play the game one more time!"
        if mode == 1:
            range100()
        elif mode == 2:
            range1000()
    

    
frame = simplegui.create_frame('Guess the number', 100, 100)

frame.add_input('',input_guess,50)
frame.add_button('Choose a positive integer from 0 to 99.',range100,250)
frame.add_button('Choose a positive integer from 0 to 999.',range1000,250)
 
new_game()
