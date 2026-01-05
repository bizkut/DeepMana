"""Effect for Wrathspine Enchanter (TSC_630).

Card Text: <b>Battlecry:</b> Cast a copy of a Fire, Frost, and Nature spell in your hand <i>(targets chosen randomly).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass