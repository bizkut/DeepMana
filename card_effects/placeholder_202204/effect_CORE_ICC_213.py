"""Effect for Eternal Servitude (CORE_ICC_213).

Card Text: <b>Discover</b> a friendly minion that died this game. Summon it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_213t")