"""Effect for Scorp-o-matic (LOOT_111).

Card Text: <b>Battlecry:</b> Destroy a minion with 1 or less Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()