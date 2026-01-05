"""Effect for Murloc Knight (AT_076).

Card Text: <b>Inspire:</b> Summon a random Murloc.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AT_076t")