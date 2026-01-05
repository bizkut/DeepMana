"""Effect for Lock and Load (CORE_AT_061).

Card Text: Each time you cast a spell this turn, get a random Hunter card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass