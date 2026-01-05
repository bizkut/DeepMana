"""Effect for Hand of Gul'dan (BT_300).

Card Text: When you play
or discard this,
draw 3 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)