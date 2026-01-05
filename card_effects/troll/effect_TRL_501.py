"""Effect for Auchenai Phantasm (TRL_501).

Card Text: <b>Battlecry:</b> This turn, your healing effects deal damage instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)