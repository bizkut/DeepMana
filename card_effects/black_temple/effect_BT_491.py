"""Effect for Spectral Sight (BT_491).

Card Text: [x]Draw a card.
<b>Outcast:</b> Draw another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)