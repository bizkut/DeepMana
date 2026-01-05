"""Effect for Broll Bearmantle (EDR_853).

Card Text: After you cast a spell, summon a random
Animal Companion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_853t")