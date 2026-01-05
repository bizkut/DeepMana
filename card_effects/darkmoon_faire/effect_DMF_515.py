"""Effect for Swindle (DMF_515).

Card Text: Draw a spell.
<b>Combo:</b> And a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)