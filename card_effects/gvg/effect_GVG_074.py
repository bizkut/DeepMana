"""Effect for Kezan Mystic (GVG_074).

Card Text: <b>Battlecry:</b> Take control of a random enemy <b>Secret</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass