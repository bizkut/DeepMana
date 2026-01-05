"""Effect for Cyborg Patriarch (TIME_046).

Card Text: <b>Dormant</b> for 3 turns.
<b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass