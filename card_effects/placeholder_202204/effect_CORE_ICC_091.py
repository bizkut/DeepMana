"""Effect for Dead Man's Hand (CORE_ICC_091).

Card Text: Shuffle a copy of your hand into your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass