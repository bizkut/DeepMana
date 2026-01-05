"""Effect for Steward of Darkshire (OG_310).

Card Text: Whenever you summon a 1-Health minion, give it <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_310t")