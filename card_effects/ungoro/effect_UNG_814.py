"""Effect for Giant Wasp (UNG_814).

Card Text: <b>Stealth</b>
 <b>Poisonous</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass