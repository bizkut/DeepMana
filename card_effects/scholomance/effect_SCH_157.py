"""Effect for Enchanted Cauldron (SCH_157).

Card Text: <b><b>Spellburst</b>:</b> Cast a random spell of the same Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass