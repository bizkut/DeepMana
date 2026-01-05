"""Effect for Forge of Souls (ICC_281).

Card Text: Draw 2 weapons from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)