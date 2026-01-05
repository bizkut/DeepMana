"""Effect for Rummaging Kobold (LOOT_389).

Card Text: <b>Battlecry:</b> Return one of your destroyed weapons to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()