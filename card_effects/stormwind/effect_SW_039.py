"""Effect for Final Showdown (SW_039).

Card Text: <b>Questline:</b> Draw 4 cards in one turn. <b>Reward:</b> Reduce the Cost of the cards drawn by (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)