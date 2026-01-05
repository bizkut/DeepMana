"""Effect for Desert Hare (ULD_719).

Card Text: <b>Battlecry:</b> Summon two 1/1 Desert Hares.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_719t")