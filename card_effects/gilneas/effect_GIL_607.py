"""Effect for Toxmonger (GIL_607).

Card Text: [x]Whenever you play a 1-Cost
minion, give it <b>Poisonous</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1