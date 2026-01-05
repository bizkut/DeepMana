"""Effect for Addled Grizzly (WON_009).

Card Text: After you summon a
Beast, give it +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_009t")