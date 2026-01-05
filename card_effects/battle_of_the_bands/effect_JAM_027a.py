"""Effect for Zok Rocks! (JAM_027a).

Card Text: Give a friendly minion +2 Attack and <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
