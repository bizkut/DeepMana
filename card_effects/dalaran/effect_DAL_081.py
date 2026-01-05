"""Effect for Spellward Jeweler (DAL_081).

Card Text: <b>Battlecry:</b> Your hero is <b>Elusive</b> until next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass