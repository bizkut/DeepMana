"""Effect for Ravenous Pterrordax (UNG_047).

Card Text: <b>Battlecry:</b> Destroy a friendly minion to <b>Adapt</b> twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()