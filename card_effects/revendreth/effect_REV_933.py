"""Effect for Imbued Axe (REV_933).

Card Text: [x]After your hero attacks,
give your damaged minions
+1/+2. <b>Infuse (2):</b>
+2/+2 instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1