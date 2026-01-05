"""Effect for Gone Fishin' (TSC_916).

Card Text: <b>Dredge</b>.
<b>Combo:</b> Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)