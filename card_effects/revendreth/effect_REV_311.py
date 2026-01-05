"""Effect for Nightshade Bud (REV_311).

Card Text: <b>Choose One - </b><b>Discover</b> a minion from your deck to summon;
or a spell to cast.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_311t")