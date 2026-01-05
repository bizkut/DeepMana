"""Effect for Moonlit Guidance (DED_002).

Card Text: [x]<b>Discover</b> a copy of
a card in your deck.
If you play it this turn,
draw the original.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)