"""Effect for Devolving Missiles (SCH_235).

Card Text: [x]Shoot three missiles
at random enemy minions
that transform them into
ones that cost (1) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass