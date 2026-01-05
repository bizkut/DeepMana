"""Effect for Blood of The Ancient One (OG_173).

Card Text: If you control two of these
at the end of your turn, merge them into 'The Ancient One'.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass