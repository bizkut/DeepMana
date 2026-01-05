"""Effect for Balloon Merchant (DMF_235).

Card Text: <b>Battlecry:</b> Give your Silver Hand Recruits +1 Attack and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1