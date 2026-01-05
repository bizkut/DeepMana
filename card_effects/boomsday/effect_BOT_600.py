"""Effect for Research Project (BOT_600).

Card Text: Each player draws 2 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)