"""Effect for Horde Operative (BAR_430).

Card Text: <b>Battlecry:</b> Copy your opponent's <b>Secrets</b> and put them into play.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass