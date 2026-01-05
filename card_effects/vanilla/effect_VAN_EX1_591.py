"""Effect for Auchenai Soulpriest (VAN_EX1_591).

Card Text: Your cards and powers that restore Health now deal damage instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)