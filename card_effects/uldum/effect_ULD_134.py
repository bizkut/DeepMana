"""Effect for BEEEES!!! (ULD_134).

Card Text: [x]Choose a minion.
Summon four 1/1 Bees
that attack it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_134t")