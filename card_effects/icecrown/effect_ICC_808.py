"""Effect for Crypt Lord (ICC_808).

Card Text: [x]<b>Taunt</b>
After you summon a minion,
 gain +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_808t")