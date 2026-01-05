"""Effect for Mark of Y'Shaarj (OG_048).

Card Text: Give a minion +2/+2.
If it's a Beast, draw
a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)