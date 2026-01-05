"""Effect for Halazzi, the Lynx (TRL_900).

Card Text: <b>Battlecry:</b> Fill your hand with 1/1 Lynxes that have <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass