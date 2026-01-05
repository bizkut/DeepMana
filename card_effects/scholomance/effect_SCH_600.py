"""Effect for Demon Companion (SCH_600).

Card Text: Summon a random Demon Companion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_600t")