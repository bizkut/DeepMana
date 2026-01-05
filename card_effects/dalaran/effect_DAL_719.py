"""Effect for Tak Nozwhisker (DAL_719).

Card Text: [x]Whenever you shuffle a
card into your deck, add
a copy to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass