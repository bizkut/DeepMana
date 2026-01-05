"""Effect for Shadow Waltz (CORE_REV_372).

Card Text: Summon a 3/5 Shadow with <b>Taunt</b>. If a minion died this turn, summon another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_372t")