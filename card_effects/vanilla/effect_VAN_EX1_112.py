"""Effect for Gelbin Mekkatorque (VAN_EX1_112).

Card Text: <b>Battlecry:</b> Summon an AWESOME invention.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "VAN_EX1_112t")