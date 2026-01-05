"""Effect for Tinkmaster Overspark (EX1_083).

Card Text: [x]<b>Battlecry:</b> Transform
another random minion
into a 5/5 Devilsaur
 or a 1/1 Squirrel.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass