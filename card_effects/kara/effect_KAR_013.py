"""Effect for Purify (KAR_013).

Card Text: <b>Silence</b> a friendly minion. Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)