"""Effect for Sleep with the Fishes (CFM_716).

Card Text: Deal $3 damage to all damaged minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)