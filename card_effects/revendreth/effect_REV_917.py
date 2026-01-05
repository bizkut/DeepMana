"""Effect for Carving Chisel (REV_917).

Card Text: After your hero attacks, summon a random basic Totem.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_917t")