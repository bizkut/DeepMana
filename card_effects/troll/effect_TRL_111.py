"""Effect for Headhunter's Hatchet (TRL_111).

Card Text: [x]<b>Battlecry:</b> If you
control a Beast, gain
+1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1