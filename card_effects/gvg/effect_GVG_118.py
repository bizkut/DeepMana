"""Effect for Troggzor the Earthinator (GVG_118).

Card Text: Whenever your opponent casts a spell, summon a Burly Rockjaw Trogg.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "GVG_118t")