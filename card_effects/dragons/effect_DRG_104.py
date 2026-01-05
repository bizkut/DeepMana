"""Effect for Chenvaala (DRG_104).

Card Text: After you cast three spells in a turn, summon a 5/5 Elemental.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_104t")