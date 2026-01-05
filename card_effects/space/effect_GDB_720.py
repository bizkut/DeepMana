"""Effect for Starlight Wanderer (GDB_720).

Card Text: <b>Battlecry:</b> The next Draenei you play gains +2/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
