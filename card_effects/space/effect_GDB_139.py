"""Effect for Libram of Faith (GDB_139).

Card Text: Summon three 3/3 Draenei with <b>Divine Shield</b>. If this costs (0), give them <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
