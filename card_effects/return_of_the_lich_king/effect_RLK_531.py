"""Effect for Infantry Reanimator (RLK_531).

Card Text: [x]<b>Battlecry:</b> Resurrect
a friendly Undead.
Give it <b>Reborn</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1