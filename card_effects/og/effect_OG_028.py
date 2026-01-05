"""Effect for Thing from Below (OG_028).

Card Text: [x]<b>Taunt</b>
Costs (1) less for each
Totem you've summoned
this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_028t")