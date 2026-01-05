"""Effect for Archmage Antonidas (EX1_559).

Card Text: Whenever you cast a spell, add a 'Fireball' spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass