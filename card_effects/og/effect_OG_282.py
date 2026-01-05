"""Effect for Blade of C'Thun (OG_282).

Card Text: <b>Battlecry:</b> Destroy a minion. Add its Attack and Health to your C'Thun's <i>(wherever it is).</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()