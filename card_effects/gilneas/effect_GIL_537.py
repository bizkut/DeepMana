"""Effect for Deadly Arsenal (GIL_537).

Card Text: Reveal a weapon from your deck. Deal its Attack to all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass