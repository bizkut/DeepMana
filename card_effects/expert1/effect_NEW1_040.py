"""Effect for Hogger (NEW1_040).

Card Text: At the end of your turn, summon a 2/2 Gnoll with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NEW1_040t")