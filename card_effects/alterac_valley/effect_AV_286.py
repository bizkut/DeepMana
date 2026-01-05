"""Effect for Felwalker (AV_286).

Card Text: <b>Taunt</b>. <b>Battlecry</b>: Cast the highest Cost Fel spell from your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass