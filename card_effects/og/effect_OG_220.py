"""Effect for Malkorok (OG_220).

Card Text: <b>Battlecry:</b> Equip a random weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass