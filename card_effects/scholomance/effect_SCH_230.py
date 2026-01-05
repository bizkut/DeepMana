"""Effect for Onyx Magescribe (SCH_230).

Card Text: <b>Spellburst:</b> Add 2 random spells from your class to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass