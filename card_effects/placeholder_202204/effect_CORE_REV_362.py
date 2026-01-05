"""Effect for Castle Kennels (CORE_REV_362).

Card Text: [x]Give a friendly minion 
+2 Attack. If it's a 
Beast, give it <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2