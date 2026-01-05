"""Effect for Deathmatch Pavilion (DMF_706).

Card Text: Summon a 3/2 Duelist.
If your hero attacked this turn, summon another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_706t")