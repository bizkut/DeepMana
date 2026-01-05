"""Effect for Solar Eclipse (CORE_DMF_058).

Card Text: The next spell you cast this turn casts twice.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass