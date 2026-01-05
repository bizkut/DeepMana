"""Effect for Faceless Shambler (OG_174).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Copy a friendly minion's Attack and Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)