"""Effect for Cathedral Gargoyle (GIL_635).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, gain <b>Taunt</b> and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass