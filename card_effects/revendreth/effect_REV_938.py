"""Effect for Door of Shadows (REV_938).

Card Text: [x]Draw a spell. <b>Infuse (2):</b>
Add a <b>Temporary</b> copy
of it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)