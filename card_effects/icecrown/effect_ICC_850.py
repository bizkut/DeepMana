"""Effect for Shadowblade (ICC_850).

Card Text: <b>Battlecry:</b> Your hero is <b>Immune</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass