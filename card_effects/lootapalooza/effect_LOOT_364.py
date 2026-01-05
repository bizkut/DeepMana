"""Effect for Reckless Flurry (LOOT_364).

Card Text: Spend all your Armor. Deal that much damage to all minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)