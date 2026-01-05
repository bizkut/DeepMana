"""Effect for Storm's Wrath (DRG_215).

Card Text: Give your minions +1/+1.
<b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1