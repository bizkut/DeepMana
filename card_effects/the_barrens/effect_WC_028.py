"""Effect for Meeting Stone (WC_028).

Card Text: [x]At the end of your turn,
add a 2/2 Adventurer
with a random bonus effect
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass