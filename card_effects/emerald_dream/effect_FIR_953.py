"""Effect for Magma Hound (FIR_953).

Card Text: [x]<b>Rush</b>. After this attacks a
minion and survives, deal this
minion's Attack damage split
among all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)