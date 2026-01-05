"""Effect for Murloc Tidecaller (VAN_EX1_509).

Card Text: Whenever a Murloc is summoned, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "VAN_EX1_509t")