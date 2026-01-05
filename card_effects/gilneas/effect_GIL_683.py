"""Effect for Marsh Drake (GIL_683).

Card Text: <b>Battlecry:</b> Summon a 2/1 <b>Poisonous</b> Drakeslayer for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GIL_683t")