"""Effect for Frozen Crusher (UNG_079).

Card Text: After this minion attacks, <b>Freeze</b> it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True