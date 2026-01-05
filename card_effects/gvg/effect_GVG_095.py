"""Effect for Goblin Sapper (GVG_095).

Card Text: Has +4 Attack while your opponent has 6 or more cards in hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4