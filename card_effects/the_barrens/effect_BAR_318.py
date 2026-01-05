"""Effect for Silverleaf Poison (BAR_318).

Card Text: [x]Give your weapon
"After your hero attacks,
draw a card."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)