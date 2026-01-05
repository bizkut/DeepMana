"""Effect for Cobalt Spellkin (DRG_075).

Card Text: <b>Battlecry:</b> Add two 1-Cost spells from your class to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass