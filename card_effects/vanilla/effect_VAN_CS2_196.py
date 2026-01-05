"""Effect for Razorfen Hunter (VAN_CS2_196).

Card Text: <b>Battlecry:</b> Summon a 1/1 Boar.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "VAN_CS2_196t")