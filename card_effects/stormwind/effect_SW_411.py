"""Effect for SI:7 Informant (SW_411).

Card Text: <b>Battlecry:</b> Gain +1/+1 for each other SI:7 card you've played this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1