"""Effect for Soldier of Fortune (DAL_771).

Card Text: Whenever this minion attacks, give your opponent a Coin.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1