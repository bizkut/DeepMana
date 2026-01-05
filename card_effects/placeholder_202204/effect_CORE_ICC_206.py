"""Effect for Treachery (CORE_ICC_206).

Card Text: Choose a friendly minion and give it to your opponent.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1