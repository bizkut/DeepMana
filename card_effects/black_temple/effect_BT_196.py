"""Effect for Keli'dan the Breaker (BT_196).

Card Text: [x]<b>Battlecry:</b> Destroy a minion.
If drawn this turn, instead
destroy all minions
except this one.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)