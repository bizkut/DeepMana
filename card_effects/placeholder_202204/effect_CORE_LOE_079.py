"""Effect for Elise Starseeker (CORE_LOE_079).

Card Text: <b>Battlecry:</b> Shuffle the 'Map to the Golden Monkey'   into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass