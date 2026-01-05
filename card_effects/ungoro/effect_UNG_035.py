"""Effect for Curious Glimmerroot (UNG_035).

Card Text: [x]<b>Battlecry:</b> Look at 3 cards.
Guess which one started
in your opponent's deck
to get a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass