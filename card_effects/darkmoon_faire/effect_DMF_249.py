"""Effect for Acrobatics (DMF_249).

Card Text: Draw 2 cards. If you play both this turn, draw 2 more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)