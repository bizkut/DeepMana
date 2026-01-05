"""Effect for Dragon Speaker (DAL_147).

Card Text: <b>Battlecry:</b> Give all Dragons in your hand +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3