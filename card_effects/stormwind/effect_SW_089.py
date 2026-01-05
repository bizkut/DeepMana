"""Effect for Entitled Customer (SW_089).

Card Text: <b>Battlecry:</b> Deal damage equal to your hand size to all other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)