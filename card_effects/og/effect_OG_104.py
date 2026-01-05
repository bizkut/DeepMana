"""Effect for Embrace the Shadow (OG_104).

Card Text: This turn, your healing effects deal damage instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)