"""Effect for Talgath (GDB_472).

Card Text: [x]Undamaged enemy minions take double damage. <b>Combo:</b> Get a Backstab.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
