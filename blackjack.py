# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.my_cards = []

    def __str__(self):
        s = ''
        for c in self.my_cards:
            s += str(c) + ' '
        return s

    def add_card(self, card):
        self.my_cards.append(card)

    def get_value(self):
        total = 0
        has_ace = False
        for c in self.my_cards:
            r = c.get_rank()
            if r == 'A':
                has_ace = True
            total += VALUES[c.get_rank()]
        if has_ace and total <= 11:
            return total + 10
        return total
   
    def draw(self, canvas, pos):
        pass    # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        print 'Making a deck'
        self.deck = []
        for r in RANKS:
            for s in SUITS:
                self.deck.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)
    
    def __str__(self):
        s = ''
        for c in self.deck:
            s += str(c) + ' '
        return s



#define event handlers for buttons
def deal():
    global d, player_hand, dealer_hand, in_play
    d = Deck()
    print d
    d.shuffle()
    print d
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2): # [0, 1]
      player_hand.add_card(d.deal_card())
      dealer_hand.add_card(d.deal_card())
    print player_hand, player_hand.get_value()
    print dealer_hand, dealer_hand.get_value()
    print d
    in_play = True

def hit():
    global player_hand, d, in_play
    if in_play == True:
        player_hand.add_card(d.deal_card())
        score = player_hand.get_value()
        print player_hand, score
        if score > 21:
            print "Busted yo. Ben sucks at life."
            in_play = False
       
def stand():
    global in_play, dealer_hand, player_hand
    if in_play == False:
        return
    in_play = False
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(d.deal_card())
    print dealer_hand, dealer_hand.get_value()
    if dealer_hand.get_value() > 21:
        print 'Player wins'
    elif dealer_hand.get_value() >= player_hand.get_value():
        print 'Dealer wins'
    else:
        print 'Player wins'

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    #card = Card("S", "A")
    x = 100
    for card in player_hand.my_cards:
        card.draw(canvas, [x, 300])
        x = x + 100
    x = 100
    for card in dealer_hand.my_cards:
        card.draw(canvas, [x, 100])
        x = x + 100


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
