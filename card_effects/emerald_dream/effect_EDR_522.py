"""Effect for Mimicry (EDR_522).

Card Text: Your opponent
draws 2 cards. You get copies of them.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)