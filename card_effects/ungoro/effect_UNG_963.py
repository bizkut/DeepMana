"""Effect for Lyra the Sunshard (UNG_963).

Card Text: Whenever you cast a spell, add a random Priest spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass