"""Effect for Scalehide Kodo (TLC_454).

Card Text: [x]<b>Battlecry:</b> Destroy the
lowest Attack enemy minion.
<b>Kindred:</b> The highest
Attack instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()