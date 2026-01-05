"""Effect for Stampede (UNG_916).

Card Text: Each time you play a Beast this turn, add a random Beast to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass