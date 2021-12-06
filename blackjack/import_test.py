import blackjack

personal_details = ("Tim", 24, "Australia")
name, _, country = personal_details
print(name, _, country)










# # when importing python module -> code loaded into memory and executed
# print(__name__)
#
# # Python has no concept of private or protected variables
# # modifying the code by dealing a card to dealer first giving him 2 also to start and not counting the first in score
# blackjack._deal_card(blackjack.dealer_card_frame)
#
# # starting the game by calling the method play_game() from imported module
# blackjack.play_game()
#
# # printing out the card objects created -> str(#), suit
# print(blackjack.cards)
#
# # name_ == if name conflicts with other names built in to python
# # ex: from_ for scrollbar
#
# # starting with a _name == meant to be treated as protected
# # Protected == is a version of public restricted only to subclasses.

## __name__ == should not be changing
## _ == throwaway
