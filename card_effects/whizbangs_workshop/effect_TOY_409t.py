"""Effect for Warsong Commander (TOY_409t).

Card Text: Whenever you summon a minion with 3 or less Attack, give it <b>Charge</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
