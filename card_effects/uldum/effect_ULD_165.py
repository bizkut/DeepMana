"""Effect for Riftcleaver (ULD_165).

Card Text: <b>Battlecry:</b> Destroy a minion. Your hero takes damage equal to its Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()