"""Effect for Druid of Regrowth (TIME_033).

Card Text: <b>Rewind</b>
<b>Battlecry:</b> Cast 2 random Nature spells.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass