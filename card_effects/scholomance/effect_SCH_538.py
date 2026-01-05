"""Effect for Ace Hunter Kreen (SCH_538).

Card Text: Your other characters are <b>Immune</b> while attacking.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass