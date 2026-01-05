"""Effect for Chief Inspector (GIL_648).

Card Text: <b>Battlecry:</b> Destroy all enemy <b>Secrets</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()