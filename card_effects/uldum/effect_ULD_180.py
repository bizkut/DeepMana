"""Effect for Sunstruck Henchman (ULD_180).

Card Text: At the start of your turn, this has a 50% chance to fall asleep.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass