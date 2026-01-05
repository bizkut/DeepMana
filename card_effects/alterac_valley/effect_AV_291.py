"""Effect for Frostsaber Matriarch (AV_291).

Card Text: [x]<b>Taunt</b>. Costs (1) less
 for each Beast you've
 summoned this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_291t")