"""Effect for Elementary Reaction (BOT_093).

Card Text: Draw a card. Copy it if you played an Elemental last turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)