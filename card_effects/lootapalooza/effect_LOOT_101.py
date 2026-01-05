"""Effect for Explosive Runes (LOOT_101).

Card Text: <b>Secret:</b> After your opponent plays a minion, deal $6 damage to it and any excess to their hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)