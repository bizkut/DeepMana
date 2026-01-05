"""Effect for Betrayal (VAN_EX1_126).

Card Text: Force an enemy minion to deal its damage to the minions next to it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)