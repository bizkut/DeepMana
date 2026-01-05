"""Effect for Dragoncaster (DRG_322).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, your next spell this turn costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass