"""Effect for Costumed Entertainer (DMF_189).

Card Text: [x]<b>Battlecry:</b> Give a random
minion in your hand +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2