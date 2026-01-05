"""Effect for Dune Sculptor (ULD_329).

Card Text: [x]After you cast a spell,
add a random Mage
minion to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass