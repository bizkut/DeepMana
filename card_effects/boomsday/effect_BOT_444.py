"""Effect for Floop's Glorious Gloop (BOT_444).

Card Text: Whenever a minion dies this turn, refresh
a Mana Crystal.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass