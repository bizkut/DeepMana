"""Effect for Loan Shark (SW_434).

Card Text: [x]<b>Battlecry:</b> Give your
opponent a Coin.
  <b>Deathrattle:</b> You get two.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1


def deathrattle(game, source):
    pass