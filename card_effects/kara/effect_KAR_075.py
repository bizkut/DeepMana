"""Effect for Moonglade Portal (KAR_075).

Card Text: Restore #6 Health. Summon a random
6-Cost minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_075t")