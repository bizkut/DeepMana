"""Effect for Brann Bronzebeard (LOE_077).

Card Text: Your <b>Battlecries</b> trigger twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass