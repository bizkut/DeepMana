"""Effect for Silas Darkmoon (DMF_074).

Card Text: <b>Battlecry:</b> Choose a direction to rotate all minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass