"""Effect for Call to Adventure (DAL_727).

Card Text: Draw the lowest Cost minion from your deck. Give it +2/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)