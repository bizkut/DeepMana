"""Effect for Undefeated Champion (TIME_872).

Card Text: [x]<b>Rush</b>. <b>Battlecry:</b> Fill your
opponent's board with
  random 1-Cost minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass