"""Effect for Imprisoned Felmaw (BT_211).

Card Text: [x]<b>Dormant</b> for 2 turns.
When this awakens,
  attack a random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass