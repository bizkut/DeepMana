"""Effect for Unsleeping Soul (DAL_065).

Card Text: <b>Silence</b> a friendly minion, then summon a copy of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_065t")