"""Effect for Kabal Crystal Runner (WON_308).

Card Text: Costs (2) less for each <b>Secret</b> you've played this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass