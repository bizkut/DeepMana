"""Effect for Shadow of Demise (RLK_567).

Card Text: Each time you cast a spell, transform this into a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass