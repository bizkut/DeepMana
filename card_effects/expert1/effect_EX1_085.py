"""Effect for Mind Control Tech (EX1_085).

Card Text: [x]<b>Battlecry:</b> If your opponent
has 4 or more minions,
take control of one.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass