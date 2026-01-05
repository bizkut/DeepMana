"""Effect for Ashtongue Battlelord (BT_423).

Card Text: <b>Taunt</b>
<b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass