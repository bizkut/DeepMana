"""Effect for Gorishi Wasp (TLC_630).

Card Text: <b>Rush</b>. Whenever this takes damage, get a 1-Cost Gorishi Stinger.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass