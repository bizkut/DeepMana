"""Effect for Life from Death (NX2_011).

Card Text: [x]Draw 3 cards.
<b>Infuse (6):</b> This costs (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)