"""Effect for Paragon of Light (GIL_685).

Card Text: While this minion has 3 or more Attack, it has <b>Taunt</b> and <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass