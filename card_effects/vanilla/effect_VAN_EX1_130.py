"""Effect for Noble Sacrifice (VAN_EX1_130).

Card Text: <b>Secret:</b> When an enemy attacks, summon a 2/1 Defender as the new target.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "VAN_EX1_130t")