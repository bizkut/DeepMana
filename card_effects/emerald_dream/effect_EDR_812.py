"""Effect for Grotesque Runeblade (EDR_812).

Card Text: [x]<b>Battlecry:</b> If the last card you
played had an Unholy rune,
gain +1 Attack. Repeat for
    Blood and +1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1