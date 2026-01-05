"""Effect for Scourge Rager (RLK_900).

Card Text: <b>Reborn</b>
<b>Battlecry:</b> Die.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass