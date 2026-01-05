"""Effect for Ravenous Devilsaur (TLC_829).

Card Text: [x]<b>Battlecry:</b> Destroy a minion.
<b>Kindred:</b> Gain its stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()