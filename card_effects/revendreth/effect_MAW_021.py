"""Effect for Clear Conscience (MAW_021).

Card Text: Give a friendly minion +2/+3 and "<b>Elusive</b> on your opponent's turn."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2