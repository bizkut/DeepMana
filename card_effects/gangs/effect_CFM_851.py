"""Effect for Daring Reporter (CFM_851).

Card Text: Whenever your opponent draws a card, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)