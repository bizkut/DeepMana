"""Effect for Eerie Statue (LOE_107).

Card Text: Can’t attack unless it’s the only minion on the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass