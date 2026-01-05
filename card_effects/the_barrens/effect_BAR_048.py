"""Effect for Bru'kan (BAR_048).

Card Text: <b>Nature Spell Damage +3</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3