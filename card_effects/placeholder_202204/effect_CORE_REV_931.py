"""Effect for Conqueror's Banner (CORE_REV_931).

Card Text: Reveal a card from each player's deck, three times. Draw any of yours that cost more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)