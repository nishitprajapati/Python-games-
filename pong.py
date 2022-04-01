# Implementation of classic arcade game Pong

# 2 players can play this game using 'w' key for upward , 's; key for downward motion of left paddle and up arrow and down arrow key for right paddle.

# on below given link you can play this game

'''
https://py2.codeskulptor.org/#user48_0oKaBdylo2CaPJe.py

'''

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
L = 1
R = 0
ball_pos = [300, 200]
ball_vel = [1, 1]
score1 = 0
score2 = 0
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    if direction == "RIGHT":
        ball_vel[0] = 1
        ball_vel[1] = - 1
    elif direction == "LEFT":
        ball_vel[0] = - 1
        ball_vel[1] = - 1
    
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, L, R  # these are ints
    score1, score2 = 0, 0
    paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel = 200, 200, 0, 0
    k = random.choice(["LEFT", "RIGHT"])
    spawn_ball(k)

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 2
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 2
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

def restart():
    return new_game()
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] == 20 or ball_pos[0] == 580:
        ball_vel[0] = - ball_vel[0] 
    if ball_pos[1] == 20 or ball_pos[1] == 380:
        ball_vel[1] = - ball_vel[1]
    
        
    # draw ball
    canvas.draw_circle(ball_pos, 20, 5, "White", "Red")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    if 40 < paddle1_pos < 360:
        canvas.draw_line([0,  paddle1_pos - 40], [0, paddle1_pos + 40], 18, "White")
    else:
        paddle1_vel = 0
        if paddle1_pos <= 40:
            paddle1_pos = 40
            canvas.draw_line([0,  paddle1_pos - 40], [0, paddle1_pos + 40], 18, "White")
        elif paddle1_pos >= 360:
            paddle1_pos = 360
            canvas.draw_line([0,  paddle1_pos - 40], [0, paddle1_pos + 40], 18, "White")
            
        
    if 40 < paddle2_pos < 360:
        canvas.draw_line([WIDTH, paddle2_pos - 40], [WIDTH, paddle2_pos + 40], 18, "White")
    else:
        paddle2_vel = 0
        if paddle2_pos <= 40:
            paddle2_pos = 40
            canvas.draw_line([WIDTH,  paddle2_pos - 40], [WIDTH, paddle2_pos + 40], 18, "White")
        elif paddle2_pos >= 360:
            paddle2_pos = 360
            canvas.draw_line([WIDTH,  paddle2_pos - 40], [WIDTH, paddle2_pos + 40], 18, "White")

    
    # determine whether paddle and ball collide
    
    if ball_pos[0] == 38 and paddle1_pos - 40 < ball_pos[1] < paddle1_pos + 40:
        ball_vel[0] = - ball_vel[0]
            
        
         
    if ball_pos[0] == 562 and paddle2_pos - 40 < ball_pos[1] < paddle2_pos + 40:
        ball_vel[0] = - ball_vel[0]
         
    
    # draw scores
    if ball_pos[0] == 28 and 0 <= ball_pos[1] <= 400:
        score2 += 1
        spawn_ball("RIGHT")
    if ball_pos[0] == 572 and 0 <= ball_pos[1] <= 400:
        score1 += 1
        spawn_ball("LEFT")
    
    canvas.draw_text(str(score1),[150, 100], 70, "White")
    canvas.draw_text(str(score2),[450, 100], 70, "White")    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("RESTART", restart)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
