"""Effect for Scourgelord Garrosh (ICC_834).

Card Text: <b>Battlecry</b>: Equip a 4/3 Shadowmourne that also damages adjacent minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass