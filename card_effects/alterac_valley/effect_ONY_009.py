"""Effect for Pet Collector (ONY_009).

Card Text: <b>Battlecry:</b> Summon a Beast from your deck that costs (5) or less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ONY_009t")