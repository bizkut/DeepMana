"""Effect for Living Dragonbreath (DRG_068).

Card Text: Your minions can't be <b>Frozen</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass