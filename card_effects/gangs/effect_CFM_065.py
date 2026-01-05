"""Effect for Volcanic Potion (CFM_065).

Card Text: Deal $2 damage to all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)