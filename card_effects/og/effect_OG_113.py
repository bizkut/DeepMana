"""Effect for Darkshire Councilman (OG_113).

Card Text: [x]After you summon a minion,
 gain +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_113t")