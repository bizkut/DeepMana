"""Effect for Ancient Mysteries (ULD_726).

Card Text: Draw a <b>Secret</b> from your deck. It costs (0).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(0)