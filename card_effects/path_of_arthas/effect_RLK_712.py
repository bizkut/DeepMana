"""Effect for Blood Tap (RLK_712).

Card Text: Give all minions in your hand +1/+1.
Spend 2 <b>Corpses</b> to give them +1/+1 more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1