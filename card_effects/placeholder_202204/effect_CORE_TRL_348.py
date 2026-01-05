"""Effect for Springpaw (CORE_TRL_348).

Card Text: [x]<b>Rush</b>
<b>Battlecry:</b> Add a 1/1 Lynx
with <b>Rush</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass