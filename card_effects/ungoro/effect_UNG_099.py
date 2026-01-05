"""Effect for Charged Devilsaur (UNG_099).

Card Text: <b>Charge</b>
<b>Battlecry:</b> Can't attack heroes this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass