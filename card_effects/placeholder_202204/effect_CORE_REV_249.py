"""Effect for The Light! It Burns! (CORE_REV_249).

Card Text: [x]Deal damage to a minion
 equal to its Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)