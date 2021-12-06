import tkinter as tk
import pygame
import random

leaderboard = []
player_Count = 0
default_name = "Player{}".format(player_Count)
starting_score = 0
kings_count = 0
game_over = False
blank_space = " "
music_play_count = 0
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Willi\Desktop\Code\Music\Travis Scott - SICKO MODE (Audio).mp3")


def shuffle():
    random.shuffle(deck)


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 - 10
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = "cards/{}_{}.{}".format(card, suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    # pop the next card off te top of the deck
    next_card = deck.pop(0)
    # and append back to bottom of deck
    deck.append(next_card)
    # add image to a label and display the label
    tk.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the cards face value
    return next_card


def display_drunkest():
    print(leaderboard[player_Count - 1].name)


def king_pulled():
    global game_over
    global kings_count
    kings_count += 1
    if kings_count == 4:
        game_over = True


class Player(object):
    global default_name
    current_player_card = None

    def __init__(self, name=default_name, drink=0, place=player_Count, mate=None, score=starting_score,
                 question_master=False, current_player_card=None):
        self.name = name
        self.drink = drink
        self.place = place
        self.mate = mate
        self.score = score
        self.question_master = question_master
        self.current_player_card = current_player_card

    def add_drink(self):
        self.drink = self.drink + 1

    def add_mate(self, player2):
        self.mate = player2.name

    def is_question_master(self):
        self.question_master = True


def add_player():
    global player_Count
    name = input("Please Enter Player Name: ")
    if name == "":
        name = default_name
    Player(name)
    leaderboard.append(Player(name))
    player_Count += 1


def play_music():
    global music_play_count
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    elif music_play_count == 0:
        pygame.mixer.music.play()
        pygame.mixer.music.get_pos()
        music_play_count += 1
    elif music_play_count == 1:
        pygame.mixer.music.unpause()


def deal_player():
    pass


def first_deal():
    deal_player()
    current_player_card.append(_deal_card(dealer))
    

def play_game():
    first_deal()
    mainWindow.mainloop()


mainWindow = tk.Tk()
mainWindow.title(80 * blank_space + "KINGS CUP")
mainWindow.geometry('640x480-0-200')

keekeeButton = tk.Button(mainWindow, text="KeeKeeButton", command=play_music, bg='blue', fg='white')
keekeeButton.grid(row=0, column=0, sticky="ew", columnspan=8)

card_frame = tk.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

mainWindow.update()

# load cards
cards = []
load_images(cards)
# Create a new deck of cards and shuffle them
deck = list(cards)

if __name__ == '__main__':
    play_game()
