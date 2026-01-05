"""Effect for Sleetbreaker (AV_260).

Card Text: <b>Battlecry:</b> Add a Windchill to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass