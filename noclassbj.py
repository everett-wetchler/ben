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

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#########################
# My code starts here
#########################

player_hand = []
dealer_hand = []
deck = []
in_play = False

def score_hand(hand):
    has_ace = False
    total = 0
    for card in hand:
        r, s = card
        total += VALUES[r]
        if r == 'A':
            has_ace = True
    if has_ace and total < 12:
        return total + 10
    return total

#define event handlers for buttons
def deal():
    global deck, player_hand, dealer_hand, in_play
    deck = [(r, s) for r in RANKS for s in SUITS]
    random.shuffle(deck)
    player_hand = deck[:2]  # Take first 2 cards
    dealer_hand = deck[2:4]  # Take next 2 cards
    deck = deck[4:]  # Remove those 4 cards
    in_play = True

def hit():
    global in_play, player_hand
    if not in_play:
        print 'Click "Deal" to start a new hand'
        return
    player_hand.append(deck.pop(0))
    score = score_hand(player_hand)
    if score > 21:
        print 'Player busted :( -- hand totals', score
        in_play = False
       
def stand():
    global in_play, player_hand, dealer_hand
    if not in_play:
        print 'Click "Deal" to start a new hand'
        return
    in_play = False
    while score_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop(0))
    dealer_score = score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    if dealer_score > 21:
        print 'Dealer busts with', dealer_score, '-- Player wins!'
        return
    if player_score > dealer_score:
        print 'Player wins!', player_score, 'vs', dealer_score
    elif player_score == dealer_score:
        print 'Tie with', player_score, 'each, which means dealer wins :('
    else:
        print 'Player loses :(', player_score, 'vs', dealer_score


def draw_card(canvas, r, s):
    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(r), 
                CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(s))
    canvas.draw_image(card_images, card_loc, CARD_SIZE,
        [x + CARD_CENTER[0], y + CARD_CENTER[1]], CARD_SIZE)

# draw handler    
def draw(canvas):
    global player_hand, dealer_hand
    # test to make sure that card.draw works, replace with your code below
    x = y = 50
    for card in player_hand:
        draw_card(card[0], card[1])
        x += 100
    x = 50
    y = 150
    if in_play:
        draw_card(card[0], card[1])
    else:
        draw_card(card[0], card[1])
    for card in dealer_hand[1:]:
        draw_card(card[0], card[1])
        x += 100


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


# remember to review the gradic rubric