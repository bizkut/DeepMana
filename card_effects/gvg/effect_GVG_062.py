"""Effect for Cobalt Guardian (GVG_062).

Card Text: Whenever you summon a Mech, gain <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_062t")