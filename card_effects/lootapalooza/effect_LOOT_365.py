"""Effect for Gemstudded Golem (LOOT_365).

Card Text: <b>Taunt</b>
Can only attack if you have 5 or more Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass