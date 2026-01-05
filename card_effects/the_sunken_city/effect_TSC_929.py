"""Effect for Emergency Maneuvers (TSC_929).

Card Text: <b>Secret:</b> When a friendly minion dies, summon a copy of it.
It's <b>Dormant</b> for 1 turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_929t")