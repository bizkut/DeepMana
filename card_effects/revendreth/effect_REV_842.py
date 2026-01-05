"""Effect for Promotion (REV_842).

Card Text: [x]Give a Silver Hand
Recruit +3/+3
and <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3