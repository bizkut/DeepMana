"""Effect for Lor'themar Theron (RLK_593).

Card Text: <b>Battlecry:</b> Double the stats of all minions in your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass