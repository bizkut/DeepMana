"""Effect for Paralytic Poison (BAR_321).

Card Text: [x]Give your weapon +1
Attack and "Your hero is
<b>Immune</b> while attacking."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1