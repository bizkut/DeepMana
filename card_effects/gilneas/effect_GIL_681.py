"""Effect for Nightmare Amalgam (GIL_681).

Card Text: <i>This has all minion types.</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass