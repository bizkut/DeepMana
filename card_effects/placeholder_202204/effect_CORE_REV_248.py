"""Effect for Boon of the Ascended (CORE_REV_248).

Card Text: Give a minion +2 Health. Summon a Kyrian with its stats and <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_248t")