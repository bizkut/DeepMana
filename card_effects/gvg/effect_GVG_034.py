"""Effect for Mech-Bear-Cat (GVG_034).

Card Text: Whenever this minion takes damage, add a <b>Spare Part</b> card to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass