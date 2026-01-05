"""Effect for Defrost (RLK_101).

Card Text: Draw a card.
Spend 2 <b>Corpses</b> to draw another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)