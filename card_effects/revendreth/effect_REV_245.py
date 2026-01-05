"""Effect for Impending Catastrophe (REV_245).

Card Text: Draw a card. Repeat for each Imp you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)