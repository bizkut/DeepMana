"""Effect for Hand of A'dal (BT_292).

Card Text: Give a minion +2/+1.
Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)