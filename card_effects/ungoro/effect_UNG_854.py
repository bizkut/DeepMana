"""Effect for Free From Amber (UNG_854).

Card Text: <b>Discover</b> a minion that costs (8) or more. Summon it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_854t")