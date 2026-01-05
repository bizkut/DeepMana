"""Effect for Big Game Hunter (VAN_EX1_005).

Card Text: <b>Battlecry:</b> Destroy a minion with 7 or more Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()