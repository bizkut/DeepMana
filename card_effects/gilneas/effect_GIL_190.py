"""Effect for Nightscale Matriarch (GIL_190).

Card Text: Whenever a friendly minion is healed, summon a 3/3 Whelp.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_190t")