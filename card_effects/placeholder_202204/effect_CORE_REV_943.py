"""Effect for Relic of Phantasms (CORE_REV_943).

Card Text: Summon two 1/1
Spirits. Improve your future Relics.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_943t")