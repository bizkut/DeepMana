"""Effect for Splitting Image (TRL_400).

Card Text: <b>Secret:</b> When one of your minions is attacked, summon a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_400t")