DEFAULT_NUMBER_OF_PLAYERS = 8


class Player:
    def __init__(self, name):
        self.name = player_name
        self.drinkscore = 0


if __name__ == "__main__":

    player_name = input("EnterName: ")
    number_of_players = input("Please Enter Amount of Players: ")

    Player = Player(player_name)
    print(Player.__dict__)

