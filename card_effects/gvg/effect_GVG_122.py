"""Effect for Wee Spellstopper (GVG_122).

Card Text: Adjacent minions
have <b>Elusive</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass