"""Effect for Hex Lord Malacrass (TRL_318).

Card Text: <b>Battlecry</b>: Add a copy of your opening hand to your hand <i>(except this card)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass