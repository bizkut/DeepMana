"""Effect for Herald Volazj (OG_316).

Card Text: <b>Battlecry:</b> Summon a 1/1 copy of each of your other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_316t")