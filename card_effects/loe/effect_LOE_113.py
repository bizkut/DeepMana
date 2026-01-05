"""Effect for Everyfin is Awesome (LOE_113).

Card Text: Give your minions +2/+2.
Costs (1) less for each Murloc you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2