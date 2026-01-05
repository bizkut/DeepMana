"""Effect for Feast of Souls (BT_427).

Card Text: Draw a card for each friendly minion that died this turn.@ <i>(@)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)