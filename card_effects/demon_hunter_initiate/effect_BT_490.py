"""Effect for Consume Magic (BT_490).

Card Text: <b>Silence</b> an enemy minion.
<b>Outcast:</b> Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)