"""Effect for Zayle, Shadow Cloak (DAL_800).

Card Text: You start the game with one of Zayle's EVIL Decks!
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass