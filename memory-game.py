# implementation of card game - Memory

# this is a memory game
# by clicking on the card, you can flip and see the 2 card in a row. if third card will not match the last flipped card, other last 2 cards will be covered again and 
# you can go on flipping the cards and match according to your memory of same card. no of turns will be upadated as you go on flipping the card
# lower the turns, better the player

# on below given web link, you can play the game by pressing play button on code skulptor

'''
https://py2.codeskulptor.org/#user48_veMZPwJiFBtnSpU.py

'''

import simplegui
import random

################################################################################################

# global variables


num_lst = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
random.shuffle(num_lst)

cen = []
# creating center points for numbers to be printed and store it in a list
ref = 15
for i in range(len(num_lst)):
    cen.append((ref,60))
    ref += 50

# creating a list for state of the card, exposed or not
exposed = []
for i in range(len(num_lst)):
    exposed.append(False)
    

# coordinate list for green polygon
cord = []
for i in range(len(num_lst)):
    q = []
    q.append([0,0])
    q.append([50,0])
    q.append([50,100])
    q.append([0,100])
    cord.append(q)
for i in range(1,len(num_lst)):
    for j in range(0,4):
        cord[i][j][0] += i * 50

        
state = 0 
turns = 0 
gm_lgc = [] # game logic list for checking if last two card are paired or not 
count = 0 # to check whther 2 consecutive mouse click are on the same green polygon or not

###########################################################################################################

# helper function to initialize globals
def new_game():
    global num_lst, state, turns, exposed, count
    state, turns = 0, 0
    random.shuffle(num_lst)
    for i in range(len(num_lst)):
        exposed[i] = False
    
###########################################################################################################
     
# define event handlers
def mouseclick(pos):
    global state, gm_lgc, exposed, count, turns
    
    # only non exposed card click creates valid mouse click
    
    if check(pos):
        
        # on only 2 valid mouse click 'turns' is incremented
        
        count += 1
        if count == 2:
            turns += 1
            count = 0
            
            
        if state == 0:
            for i in range(len(num_lst)):
                if cord[i][0][0] < pos[0] < cord[i][1][0] and cord[i][0][1] < pos[1] < cord[i][-1][1]:
                    if not exposed[i]:
                        gm_lgc.append(i)
                        exposed[i] = True
            state  = 1       
    
        elif state == 1:
            for i in range(len(num_lst)):
                if cord[i][0][0] < pos[0] < cord[i][1][0] and cord[i][0][1] < pos[1] < cord[i][-1][1]:
                    if not exposed[i]:
                        gm_lgc.append(i)
                        exposed[i] = True
            state = 2
        
        elif state == 2:
        
        # checking whether last two exposed cards are paired or not
            if (len(gm_lgc) > 1)  and (num_lst[gm_lgc[-1]] != num_lst[gm_lgc[-2]]):
                exposed[gm_lgc[-1]] = False
                exposed[gm_lgc[-2]] = False
                gm_lgc.remove(gm_lgc[-1])
                gm_lgc.remove(gm_lgc[-1])
            
            for i in range(len(num_lst)):
                if cord[i][0][0] < pos[0] < cord[i][1][0] and cord[i][0][1] < pos[1] < cord[i][-1][1]:
                    if not exposed[i]:
                        gm_lgc.append(i)
                        exposed[i] = True
            state = 1
        
########################################################################################################################        
# checking whether last two mouse clicks are on the same card or not

def check(pos):
    for i in range(len(num_lst)):
        if cord[i][0][0] < pos[0] < cord[i][1][0] and cord[i][0][1] < pos[1] < cord[i][-1][1]:
                if exposed[i]:
                    return False
                elif not exposed[i]:
                    return True
                    
    
        
#############################################################################################################################  
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global turns
    # updating label according to latest turns
    label.set_text("Turns = "+str(turns))
    
    # numbers draw
    
    for i in range(len(num_lst)):
        canvas.draw_text(str(num_lst[i]), cen[i], 50, "white")
    
    # green polygon draw
    
    for j in range(len(num_lst)):
        if not exposed[j]:
            canvas.draw_polygon(cord[j], 2, "Red", "Green")
            

#################################################################################################################################
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
