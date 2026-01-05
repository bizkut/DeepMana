"""Effect for Brazen Zealot (ULD_145).

Card Text: Whenever you summon a minion, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_145t")