"""Effect for Gift of the Naaru (AV_330).

Card Text: [x]Restore #3 Health to
all characters. If any
are still damaged,
draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)