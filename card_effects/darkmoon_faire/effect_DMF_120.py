"""Effect for Nazmani Bloodweaver (DMF_120).

Card Text: [x]After you cast a spell,
reduce the Cost of a random
card in your hand by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass