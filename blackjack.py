# from Nishit prajapati - acmnishit@gmail.com

# this is a simple version of a blackjack game.

'''
https://py2.codeskulptor.org/#user48_X82o7Oo1OldDTel.py

'''
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    


in_play = False
msg1 = ""
msg2 = ""
score = 0
finish = True


SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


##############################################################################################################

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

##############################################################################################################################

class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        # displaying hand
        disp = "Hand contains "
        for i in range(len(self.hand)):
            disp += str(self.hand[i])
            disp += " "
        return disp

    def add_card(self, card):
        # adding a card in handlist
        self.hand.append(card)

    def get_value(self):
        ace = False
        hand_val = 0

        for card in self.hand:
            hand_val += VALUES[card.rank]
            if card.rank == 'A':
                ace = True

        if not ace:
            return hand_val
        else:
            if hand_val + 10 <= 21:
                return hand_val + 10
            else: 
                return hand_val

    def draw(self, canvas, pos):
        num = 0
        for card in self.hand:
            card.draw(canvas, [pos[0] + num*CARD_SIZE[0], pos[1]])
            num += 1

############################################################################## 

class Deck:
    def __init__(self):
        # creating a Deck list
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # popping out last card in deck to deal
        return self.deck.pop()

    # really it is not needed for our game implementation, as we are drawing the cards
    def __str__(self):
        # displaying the deck
        disp = "Deck contains "
        for i in self.deck:
            disp += str(i)
            disp += " "
        return disp


##################################################################################################

def deal():
    global msg1, msg2, in_play, deck, playerhand, dealerhand, finish, score
    msg2 = ""
    if not finish:
        score -= 1
        msg2 = "you let off the previous hand!"
        
    deck = Deck()
    deck.shuffle()
    
    playerhand = Hand()
    dealerhand = Hand()
    
    for i in range(2):
        playerhand.add_card(deck.deal_card())
        dealerhand.add_card(deck.deal_card())
        
        
    in_play = True
    msg1 = "hit or stand?"
    finish = False
    
#######################################################################################################

def hit():
    global deck, playerhand, msg1, msg2, in_play, score, finish
    if playerhand.get_value() <= 21:
        if in_play and playerhand.get_value() <= 21:
            playerhand.add_card(deck.deal_card())
        if playerhand.get_value() > 21:
            msg2 = "You have busted!"
            score -= 1
            msg1 = "new Deal?"
            in_play = False
            finish = True
            
###########################################################################################################
    
def stand():
    global playerhand, dealerhand, deck, msg1, msg2, in_play, score, finish
    in_play = False
    if not finish:
        if playerhand.get_value() > 21:
            msg2 = "You have busted!"
            score -= 1
            finish = True
        else:
            while dealerhand.get_value() < 17:
                dealerhand.add_card(deck.deal_card())

        if dealerhand.get_value() > 21:
            msg2 = "Dealer busted! You win."
            score += 1
            finish = True
        else:
            if playerhand.get_value() > dealerhand.get_value():
                msg2 = "You win."
                score += 1
            else:
                msg2 = "It is tie."
                score -= 1
            finish = True
        msg1 = "new deal?"

    
############################################################################################################   

def draw(canvas):
    global playerhand, dealerhand
    
    canvas.draw_text("*Blackjack*", [185, 50], 55, "Black")
    canvas.draw_text(msg1, [200,356], 30, "Black")
    canvas.draw_text("Dealer:", [75,180], 30, "yellow")
    canvas.draw_text("Player:", [75, 260 + CARD_SIZE[1]], 30, "yellow")
    canvas.draw_text(msg2, [200,180], 30, "Black")
    canvas.draw_text("SCORE:", [350, 250], 40, "White")
    canvas.draw_text(str(score), [510, 250], 40, "Fuchsia")
    
    dealerhand.draw(canvas, [75,200])
    playerhand.draw(canvas, [75, 290 + CARD_SIZE[1]])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [75+CARD_SIZE[0]/2,200+CARD_SIZE[1]/2], CARD_BACK_SIZE)

############################################################################################################################################
# frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# buttons
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# starting the game
deal()
frame.start()
