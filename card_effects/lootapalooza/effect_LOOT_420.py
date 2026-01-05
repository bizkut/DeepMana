"""Effect for Skull of the Man'ari (LOOT_420).

Card Text: At the start of your turn, summon a Demon from your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_420t")