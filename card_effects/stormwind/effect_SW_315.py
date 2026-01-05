"""Effect for Alliance Bannerman (SW_315).

Card Text: [x]<b>Battlecry:</b> Draw a minion.
Give minions in your
hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)