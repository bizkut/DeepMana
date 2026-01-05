"""Effect for Skull of Gul'dan (BT_601).

Card Text: Draw 3 cards.
<b>Outcast:</b> Reduce their Cost by (3).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)