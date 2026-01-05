"""Effect for Lightning Breath (DRG_219).

Card Text: [x]Deal $4 damage to a
minion. If you're holding
a Dragon, also damage
its neighbors.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)