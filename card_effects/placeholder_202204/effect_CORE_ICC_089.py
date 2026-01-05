"""Effect for Ice Fishing (CORE_ICC_089).

Card Text: Draw 2 Murlocs from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)