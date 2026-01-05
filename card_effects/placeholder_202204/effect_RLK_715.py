"""Effect for Runeforging (RLK_715).

Card Text: Draw a weapon.
Spend a <b>Corpse</b> to reduce its Cost by (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)