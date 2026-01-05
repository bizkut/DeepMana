"""Effect for Snowfury Giant (ICC_090).

Card Text: Costs (1) less for each Mana Crystal you've <b><b>Overload</b>ed</b> this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass