"""Effect for Dispatch Kodo (CFM_335).

Card Text: <b>Battlecry:</b> Deal damage equal to this minion's Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)