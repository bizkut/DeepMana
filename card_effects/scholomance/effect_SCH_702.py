"""Effect for Felosophy (SCH_702).

Card Text: [x]Copy the lowest Cost
Demon in your hand.
<b>Outcast:</b> Give both +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1