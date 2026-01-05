"""Effect for Cloakscale Chemist (BOT_414).

Card Text: <b>Stealth</b>
<b>Divine Shield</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass