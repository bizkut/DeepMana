"""Effect for Thunder Bluff Valiant (WON_085).

Card Text: <b>Battlecry and Inspire:</b>
Give your Totems
+2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2