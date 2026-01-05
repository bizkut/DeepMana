"""Effect for Trick Totem (SCH_537).

Card Text: At the end of your turn, cast a random spell that costs (3) or less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass