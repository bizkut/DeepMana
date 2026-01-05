"""Effect for Mind Eater (RLK_845).

Card Text: <b>Deathrattle:</b> Add a copy of a card in your opponent's deck to your hand.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass