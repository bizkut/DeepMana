"""Effect for Saboteur (AT_086).

Card Text: <b>Battlecry:</b> Your opponent's Hero Power costs (5) more next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass