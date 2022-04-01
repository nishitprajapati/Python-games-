# Rock-paper-scissors-lizard-Spock mini project week 1
# from Nishit Prajapati - acmnishit@gmail.com

# run this code file on below given link
# by repeatedly pressing play button on code skulptor, you will see the game working
'''
https://py2.codeskulptor.org/#user48_yiAdqXX7EygFs8m.py

'''
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
# following function converts input name to number for
# for calculation
def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'Invalid input'

# following function converts number to name 
# for printing at last after calculations are done
def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'Invalid input'

# 1. following function takes user's choice (name string)
# 2. and generates computer random choice
# 3. and computes and prints outcome of a game
# logic - 
#1. player number and computer numbers are claculated
#2. 0, 1, 2, 3, 4 are used in loop as written
#3. for each number, preceding two numbers are winner case
#   and following two numbers are loser cases
#4. for each user input cases from 0 to 4, five cases from
#   from computer generated random choice is possible.
#5. those possible 5 cases are written as a if, elif, and else
#   statements, which includes 'tie' case also
#6. if 'if , elif, else' conditions are satisfied,
#   according to that print statements are written
#   to show user and computer choice and outcome of game 
#   for that particular choice.
def rpsls(player_choice): 
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    #1st case
    if player_number == 0 and comp_number == 4:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 0 and comp_number == 3:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 0 and comp_number == 1:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 0 and comp_number == 2:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    
    elif player_number == 0 and comp_number == 0:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player and computer tie!'
        print ' '
    #2nd case
    elif player_number == 1 and comp_number == 0:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 1 and comp_number == 4:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 1 and comp_number == 2:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 1 and comp_number == 3:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 1 and comp_number == 1:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player and computer tie!'
        print ' '
    #3rd case
    elif player_number == 2 and comp_number == 1:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 2 and comp_number == 0:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 2 and comp_number == 3:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 2 and comp_number == 4:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 2 and comp_number == 2:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player and computer tie!'
        print ' '
    #4th case
    elif player_number == 3 and comp_number == 2:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 3 and comp_number == 1:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 3 and comp_number == 4:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 3 and comp_number == 0:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 3 and comp_number == 3:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player and computer tie!'
        print ' '
    #5th case
    elif player_number == 4 and comp_number == 3:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 4 and comp_number == 2:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player wins!'
        print ' '
    elif player_number == 4 and comp_number == 0:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 4 and comp_number == 1:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Computer wins!'
        print ' '
    elif player_number == 4 and comp_number == 4:
        print 'Player chooses '+player_choice
        print 'Computer chooses '+comp_choice
        print 'Player and computer tie!'
        print ' '
    else:
        return 'Inavlid input'
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
