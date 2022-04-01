# mini-project week 3 from Nishit Prajapati
# acmnishit@gmail.com

# in the dialogue box, you have to enter a number
# according to your guess, If that number matches with
# computer gussed number, then you win the game
# you would have 7 maximum try in a game
 

# you can go on the link below and play the game  
  
'''
https://py2.codeskulptor.org/#user48_Ot18neLUidGWogs.py

'''
    
###########################################

# input will come from buttons and an input field
# all output for the game will be printed in the console

############################################

import simplegui

# random module is secretely guessing no for computer

import random

# global variable secret_number for computer 
# generated random guess

secret_number = 0

# global variable count for counting remaining
# turns for guesses by user

count = 0

# helper function to start and restart the game

def new_game():
    return range100()

# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and
    # starts a new game
    
    print "New game has started in range [0, 100)"
    print "Your remaining guesses are 7."
    print "plz enter your guessed number"
    print " "
    global secret_number
    global count
    count = 7
    secret_number = random.randrange(0, 100)
    

def range1000():
    # button that changes the range to [0,1000) and
    # starts a new game
    
    print "New game has started in range[0, 1000)"
    print "Your remaning guesses are 10."
    print "Plz Enter your guessed number"
    print " "
    global secret_number
    global count
    count = 10
    secret_number = random.randrange(0, 1000)
    
def input_guess(guess):
    # global variables
    
    global secret_number
    
    global count
    
    # converting input guess string into integer number
    
    input_number = int(guess)
    print "Your guess was",input_number
    
    #every time user enters guess, counter is decremented
    
    count -= 1
    
    #variable assignment for less crowdy coding space 
    
    a = input_number
    b = secret_number
    
    #main decision making starts here
    # if according to range, count is within limits,
    # then "if" is executed
    # no of turns(count) are 7 for "0 to 100" and
    # 10 for "0 to 1000"
    
    # if computer guess is between "0 to 100",
    # then 1st "if is executed
    # if input is also within the same range,
    # then decision is made
    
    if (count > 0) and (0 <= b < 100):
        if 0 <= a < 100:
            if b < a:
                print "Lower"
                print "Your remaining guesses are",count 
                print " "
                return " "
            elif b > a:
                print "Higher"
                print "Your remaining guesses are",count 
                print " "
                return " "
            else:
                print "Correct"
                print " "
                return range100()
        else:
            print "Guess not in range"
            print "Your remaining guesses are",count
            print " "
            return " "
    elif (count == 0) and (0 <= b < 100):
        if 0 <= a < 100:
            if b < a:
                print "Lower"
                print "You are out of turns. You lost."
                print " "
                return range100()
            elif b > a:
                print "Higher"
                print "You are out of turns. You lost."
                print " "
                return range100()
            else:
                print "Correct"
                print " "
                return range100()
        #if input is not in range 0 to 100, 
        # then error message is displayed
        
        else:
            print "Guess not in range"
            print "You are out of turns. You lost game."
            print " "
            return range100()
    
    #############################################
    # same logic is repeated for 0 to 1000
    #############################################
    elif (count > 0) and (0 <= b < 1000):
        if 0 <= a < 1000:
            if b < a:
                print "Lower"
                print "Your remaining guesses are",count 
                print " "
                return " "
            elif b > a:
                print "Higher"
                print "Your remaining guesses are",count 
                print " "
                return " "
            else:
                print "Correct"
                print " "
                return range1000()
        else:
            print "Guess not in range"
            print "Your remaining guesses are",count
            print " "
            return " "
    elif (count == 0) and (0 <= b < 1000):
        if 0 <= a < 100:
            if b < a:
                print "Lower"
                print "You are out of turns. You lost."
                print " "
                return range1000()
            elif b > a:
                print "Higher"
                print "You are out of turns. You lost."
                print " "
                return range1000()
            else:
                print "Correct"
                print " "
                return range1000()
        #if input is not in range 0 to 100, 
        # then error message is displayed
        
        else:
            print "Guess not in range"
            print "You are out of turns. You lost game."
            print " "
            return range1000()
    
# create frame

check = simplegui.create_frame("guess the number", 200, 200)

####register event handlers for control elements and
# start frame

# buttons to play in either "0 t0 100" or
# "0 to 1000" range

check.add_button("Play in range [0, 100)", range100, 100)

check.add_button("Play in range [0, 1000)", range1000, 100)

# input field for user guess

check.add_input("enter your guess here", input_guess, 200)

#frame is started

check.start()

# calls new_game whenever program is run again

new_game()


# always remember to check your completed program against the grading rubric
