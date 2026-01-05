"""Effect for Augmented Elekk (BOT_559).

Card Text: Whenever you shuffle a card into a deck, shuffle in an extra copy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass