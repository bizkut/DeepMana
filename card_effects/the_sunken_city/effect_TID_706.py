"""Effect for Herald of Chaos (TID_706).

Card Text: [x]<b>Lifesteal</b>
<b>Battlecry:</b> If you've cast a
Fel spell while holding this,
gain <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass