"""Effect for TREEEES!!! (TLC_230).

Card Text: Choose a minion. Summon four 2/2 Treants that attack it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_230t")