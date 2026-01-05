"""Effect for Reckless Diretroll (TRL_551).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Discard your lowest Cost card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass