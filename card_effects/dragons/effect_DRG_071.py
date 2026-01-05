"""Effect for Bad Luck Albatross (DRG_071).

Card Text: <b>Deathrattle:</b> Shuffle two 1/1 Albatross into your opponent's deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass