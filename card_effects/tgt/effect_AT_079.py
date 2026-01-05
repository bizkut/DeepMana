"""Effect for Mysterious Challenger (AT_079).

Card Text: <b>Battlecry:</b> Put one of each <b>Secret</b> from your deck into the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass