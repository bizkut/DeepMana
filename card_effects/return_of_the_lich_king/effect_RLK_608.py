"""Effect for Asvedon, the Grandshield (RLK_608).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Cast a copy
of the last spell your opponent played.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass