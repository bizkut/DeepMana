"""Effect for Commander Rhyssa (DAL_573).

Card Text: Your <b>Secrets</b> trigger twice.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass