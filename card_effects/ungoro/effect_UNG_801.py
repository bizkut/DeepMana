"""Effect for Nesting Roc (UNG_801).

Card Text: <b>Battlecry:</b> If you control at least 2 other minions, gain <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass