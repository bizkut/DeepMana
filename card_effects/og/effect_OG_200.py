"""Effect for Validated Doomsayer (OG_200).

Card Text: At the start of your turn, set this minion's Attack to 7.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass