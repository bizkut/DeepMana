"""Effect for Silver Hand Knight (VAN_CS2_151).

Card Text: <b>Battlecry:</b> Summon a 2/2 Squire.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "VAN_CS2_151t")