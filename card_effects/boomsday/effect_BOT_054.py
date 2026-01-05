"""Effect for Biology Project (BOT_054).

Card Text: Each player gains 2 Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass