"""Effect for Play Dead (CORE_ICC_052).

Card Text: Trigger a friendly minion's <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass