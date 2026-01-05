"""Effect for Anyfin Can Happen (LOE_026).

Card Text: Summon 7 Murlocs that died this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOE_026t")