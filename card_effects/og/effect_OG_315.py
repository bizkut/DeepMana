"""Effect for Bloodsail Cultist (OG_315).

Card Text: <b>Battlecry:</b> If you control another Pirate, give your weapon +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1