"""Effect for Clawfury Adept (AV_294).

Card Text: <b>Battlecry:</b> Give all other friendly characters +1 Attack this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1