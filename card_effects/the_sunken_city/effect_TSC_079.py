"""Effect for Radar Detector (TSC_079).

Card Text: [x]Scan the bottom 5 cards
of your deck. Draw any
Mechs found this way,
then shuffle your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)