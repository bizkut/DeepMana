"""Effect for Field of Strife (AV_661).

Card Text: [x]Your minions have
+1 Attack.
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1