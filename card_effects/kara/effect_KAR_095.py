"""Effect for Zoobot (KAR_095).

Card Text: <b>Battlecry:</b> Give a random friendly Beast, Dragon, and Murloc +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1