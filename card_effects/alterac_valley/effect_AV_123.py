"""Effect for Sneaky Scout (AV_123).

Card Text: [x]<b>Stealth</b>
<b>Honorable Kill:</b> Your next
Hero Power costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass