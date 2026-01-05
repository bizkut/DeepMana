"""Effect for The Fires of Zin-Azshari (TSC_944).

Card Text: Replace your deck with minions that cost (5) or more. They cost (5).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass