"""Effect for Ironwood Golem (LOOT_048).

Card Text: <b>Taunt</b>
Can only attack if you have 3 or more Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass