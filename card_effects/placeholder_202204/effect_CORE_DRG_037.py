"""Effect for Flik Skyshiv (CORE_DRG_037).

Card Text: [x]<b>Battlecry:</b> Destroy a
minion and all copies of it
<i>(wherever they are)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()