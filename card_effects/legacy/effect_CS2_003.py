"""Effect for Mind Vision (CS2_003).

Card Text: Put a copy of a random card in your opponent's hand into your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass