"""Effect for Ravasaur Runt (UNG_009).

Card Text: <b>Battlecry:</b> If you control at least 2 other minions, <b>Adapt.</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass