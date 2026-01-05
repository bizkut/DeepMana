"""Effect for War Master Voone (TRL_328).

Card Text: <b>Battlecry:</b> Copy all
Dragons in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass