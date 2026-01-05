"""Effect for Ratcatcher (GIL_515).

Card Text: <b>Rush</b>
<b>Battlecry:</b> Destroy a friendly minion and gain its Attack and Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()