"""Effect for Untamed Beastmaster (TRL_405).

Card Text: Whenever you draw a Beast, give it +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)