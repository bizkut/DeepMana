"""Effect for Necrium Vial (BOT_508).

Card Text: Trigger a friendly minion's <b>Deathrattle</b> twice.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass