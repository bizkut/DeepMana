"""Effect for Charred Chameleon (FIR_908).

Card Text: <b>Battlecry:</b> If you've used
your Hero Power this turn,
give a friendly minion
+1/+2 and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1