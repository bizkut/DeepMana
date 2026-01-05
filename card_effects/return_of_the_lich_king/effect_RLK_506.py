"""Effect for Boneguard Commander (RLK_506).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Raise up to
6 <b>Corpses</b> as 1/3 Risen Footmen with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass