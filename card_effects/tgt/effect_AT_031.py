"""Effect for Cutpurse (AT_031).

Card Text: Whenever this minion attacks a hero, add the Coin to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass