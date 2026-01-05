"""Effect for Portal Overfiend (DAL_565).

Card Text: [x]<b>Battlecry:</b> Shuffle 3 Portals
into your deck. When drawn,
summon a 2/2 Demon
with <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)