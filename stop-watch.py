# mini project: stop watch game => from nishit prajapati
# acmnishit@gmail.com

# if you stop the stop watch on whole seconds, you will get points

# you can play this game on below given link

'''
https://py2.codeskulptor.org/#user48_oWvDlMWZN2x1614_0.py

'''


import simplegui

# define global variables

# t is variable for calculating tick

t = 0

# tenth is variable for formatting t (tenth of second)

tenth = 0

# sec is variable for formatting seconds

sec = 0

# min = minutes, is used for formatting minutes

min = 0

# success is variable used for counting no of success at game
# it is updated when stop button is pressed and sec % 5 = 0
# and tenth = 0

success = 0

# attempt is variable used for counting total attempt at game
# meaning whenever apprpriately stop button is pressed

attempt = 0

# check variable is used for checking whether stop button
# is not used continuously more than once while watch is stopped
# it is made false here, because, when program starts
# pressing stop button should not update score
# it should update score only after watch starts

check = False

# count is used for counting seconds, whenever it becomes 10, 
# second is inceremented and count is again assigned 0

count = 0
# this is a formatting function fro deciding when to and
# how to count minute and seconds andd tenth of second

def format():
    
    global t, tenth, sec, min, count
    
# tenth should be updated at every tick, but only in range 
# 0 to 9, so we take modulo 10 any t and it returns only 0 to 9
# because for int munbers, modulo 10 can not return more than 9 
    
    tenth = t % 10
    count += 1

# I have designed this counter to work for 10 minutes and then it resets
    
    if min == 10 and sec == 0 and tenth == 0:
        reset()
        return start()
    
# if count becomes 10 means t = 10, then second is incremented 
# only if seconds is less than 59
# so it increments upto 59

    elif count == 10 and sec < 59:
        sec += 1
        count = 0

# whenever second becomes 59 and count is 10
# minute is incremented
# and second is assigned 0 and count is made 0

    elif sec == 59 and count == 10 and min < 10:
        min, sec, count = min + 1, 0, 0
        
     
# this is start handler, which starts the timer and
# sets check = true, so whenever stop button is pressed,
# it can update success and attempt

def start():
    global check
    timer.start()
    check = True
    

# this is stop function, which stops watch at that instant
# and checks if stop was stopped at right instant to win game
# if it was stopped at time % 5 = 0, 
# then user's success is incremented
# after one stop button press, check is made false,
# toprevent user from winning more than once at same attempt 

def stop():
    global success, attempt, check
    global tenth, sec
    timer.stop()
    if check == True:
        attempt += 1
        if tenth == 0:
            success += 1
        check = False
    return check
    
# this is reset function, which resets the watch to 0:00.0
# by assigning every variable 0
# check is assigned False, because if not, 
# it would update success and attempt
# without starting watch, which is not practical
    
def reset():
    timer.stop()
    global t, tenth, sec, min
    global success, attempt, check
    t, tenth, sec, min = 0, 0, 0, 0
    success, attempt, check = 0, 0, False
    
    

# tick function is called every 0. second to increment t and
# return format function, which formats time according to our needs
def tick():
    global t
    t += 1
    return format()

# draw handler draws text according our format
def draw(canvas):
    global tenth, sec, min, success, attempt
    # it formats time to set leading zeros
    
    if sec < 10:
        k = str(min)+":0"+str(sec)+"."+str(tenth)
        canvas.draw_text(k, [75,120], 60, "Red")
     
        
    # it formats if second is more than 9,
    # because then there is no need of leading zeros
    
    elif sec > 9:
        k = str(min)+":"+str(sec)+"."+str(tenth)
        canvas.draw_text(k, [75,120], 60, "Red")
     
    # it draws game score
    
    if attempt == 0:
        u = "0/0"
        canvas.draw_text(u, [230, 50], 40, "White")
    elif attempt > 0:
        u = str(success)+"/"+str(attempt)
        canvas.draw_text(u, [230, 50], 40, "White")
    
    
    
# create frame

frame = simplegui.create_frame("Stopwatch game", 300, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers

frame.set_draw_handler(draw)
frame.add_button("START", start, 100)
frame.add_button("STOP", stop, 100)
frame.add_button("RESET", reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
