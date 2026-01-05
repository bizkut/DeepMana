"""Effect for Temporus (LOOT_538).

Card Text: <b>Battlecry:</b> Your opponent takes two turns. Then you take two turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass