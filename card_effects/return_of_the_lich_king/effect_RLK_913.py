"""Effect for Overlord Drakuru (RLK_913).

Card Text: [x]<b>Rush</b>, <b>Windfury</b>
After this attacks and kills
a minion, resurrect it
on your side.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass