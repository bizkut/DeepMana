"""Effect for Murloc Tidecaller (EX1_509).

Card Text: Whenever you summon a Murloc, gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EX1_509t")