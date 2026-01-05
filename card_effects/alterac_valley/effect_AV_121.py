"""Effect for Gnome Private (AV_121).

Card Text: [x]<b>Honorable Kill:</b> Gain
+2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2