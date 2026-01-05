"""Effect for Houndmaster (VAN_DS1_070).

Card Text: <b>Battlecry:</b> Give a friendly Beast +2/+2 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2