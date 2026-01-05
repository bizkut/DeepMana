"""Effect for Kazakusan (ONY_005).

Card Text: [x]<b>Battlecry:</b> If you played 4
other Dragons this game,
craft a custom deck
of Treasures.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass