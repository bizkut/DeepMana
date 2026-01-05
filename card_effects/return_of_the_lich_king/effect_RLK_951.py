"""Effect for Coroner (RLK_951).

Card Text: <b>Battlecry:</b> <b>Freeze</b>
an enemy minion.
<b>Manathirst (6):</b>
<b>Silence</b> it first.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)