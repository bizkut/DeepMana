"""Effect for Furbolg Mossbinder (LOOT_150).

Card Text: <b>Battlecry:</b> Transform a friendly minion into a 6/6 Elemental.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass