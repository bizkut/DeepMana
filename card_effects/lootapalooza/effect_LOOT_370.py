"""Effect for Gather Your Party (LOOT_370).

Card Text: <b>Recruit</b> a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass