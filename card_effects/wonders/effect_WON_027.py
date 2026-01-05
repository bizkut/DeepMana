"""Effect for Time-Lost Raptor (WON_027).

Card Text: <b>Echo</b>
<b>Battlecry:</b> <b>Adapt</b> your Time-Lost Raptors.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass