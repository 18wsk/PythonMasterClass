import random
import tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 - 10
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = "cards/{}_{}.{}".format(card, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    # pop the next card off te top of the deck
    next_card = deck.pop(0)
    # and append back to bottom of deck
    deck.append(next_card)
    # add image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the cards face value
    return next_card


def score_hand(hand):
    # calculate the total score of all cards in the list.
    # only one ace can have the value of 11, and this will be reduced to 1 if the hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    global player_win
    global dealer_win
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_win += 1
        dealer_tally_label.set(dealer_win)
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
        player_win += 1
        player_tally_label.set(player_win)
    elif dealer_score > player_score:
        result_text.set("Dealer Wins!")
        dealer_win += 1
        dealer_tally_label.set(dealer_win)
    else:
        result_text.set("DRAW!")


def deal_player():
    global dealer_win
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_win += 1
        dealer_tally_label.set(dealer_win)


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global player_hand
    global dealer_hand
    global dealer_card_frame
    global player_card_frame
    global deck
    # embedded frame to hold card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")

    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def shuffle():
    random.shuffle(deck)


def play_game():
    initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()
# set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Player', background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

dealer_button = tkinter.Button(button_frame, text="Player", command=deal_player)
dealer_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=3)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=4)

tally_frame = tkinter.Frame(mainWindow, background="green")
tally_frame.grid(row=0, column=4)

player_tally_label = tkinter.IntVar()
tkinter.Label(tally_frame, text="Player Score:", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(tally_frame, textvariable=player_tally_label, background="green", fg="white").grid(row=1, column=0)

dealer_tally_label = tkinter.IntVar()
tkinter.Label(tally_frame, text="Dealer Score:", background="green", fg="white").grid(row=0, column=1)
tkinter.Label(tally_frame, textvariable=dealer_tally_label, background="green", fg="white").grid(row=1, column=1)

# load cards
cards = []
load_images(cards)
print(cards)
# Create a new deck of cards and shuffle them
deck = list(cards) + list(cards)
shuffle()

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

# initialize wins to 0
dealer_win = 0
player_win = 0

if __name__ == "__main__":
    play_game()
