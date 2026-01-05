"""Effect for Shenanigans (YOP_017).

Card Text: <b>Secret:</b> When your opponent draws their second card in a turn, transform it into a Banana.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)