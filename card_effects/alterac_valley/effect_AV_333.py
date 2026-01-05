"""Effect for Revive Pet (AV_333).

Card Text: <b>Discover</b> a friendly Beast that died this game. Summon it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_333t")