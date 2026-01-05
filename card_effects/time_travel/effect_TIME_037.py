"""Effect for Disciple of the Dove (TIME_037).

Card Text: <b>Battlecry:</b> Draw a minion. Give minions in your hand +2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)