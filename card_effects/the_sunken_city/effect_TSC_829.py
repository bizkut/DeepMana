"""Effect for Naga Giant (TSC_829).

Card Text: Costs (1) less for each Mana you've spent on spells this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass