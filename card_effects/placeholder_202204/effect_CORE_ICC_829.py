"""Effect for Uther of the Ebon Blade (CORE_ICC_829).

Card Text: <b>Battlecry:</b> Equip a 5/3 <b>Lifesteal</b> weapon.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass