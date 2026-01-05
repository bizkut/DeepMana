"""Effect for Enthusiastic Banker (SW_069).

Card Text: [x]At the end of your turn,
store a card from your deck.
<b>Deathrattle:</b> Add the stored
cards to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass