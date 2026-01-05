"""Effect for Parade Leader (DMF_520).

Card Text: After you summon a <b>Rush</b> minion, give it +2 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_520t")