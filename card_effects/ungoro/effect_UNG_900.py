"""Effect for Spiritsinger Umbra (UNG_900).

Card Text: After you summon a minion, trigger its <b>Deathrattle</b> effect.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_900t")