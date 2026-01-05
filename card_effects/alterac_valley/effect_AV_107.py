"""Effect for Glaciate (AV_107).

Card Text: <b>Discover</b> an 8-Cost minion. Summon and <b>Freeze</b> it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_107t")