"""Effect for Slumbering Sprite (EDR_469).

Card Text: [x]Starts <b>Dormant</b>.
After you use your Hero
Power, this awakens.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass