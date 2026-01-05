"""Effect for Sword Eater (DMF_521).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Equip a 3/2 Sword.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass