"""Effect for Don't Feed the Animals (DMF_090).

Card Text: Give all Beasts in your hand +1/+1.
<b>Corrupt:</b> Give them +2/+2 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1