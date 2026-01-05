"""Effect for Wilfred Fizzlebang (AT_027).

Card Text: Cards you draw from your Hero Power cost (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(0)