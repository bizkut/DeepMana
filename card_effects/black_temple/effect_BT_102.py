"""Effect for Boggspine Knuckles (BT_102).

Card Text: After your hero attacks, transform your minions into random ones that cost (1) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass