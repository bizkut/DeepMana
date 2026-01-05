"""Effect for Lord Marrowgar (RLK_085).

Card Text: [x]<b>Battlecry:</b> Raise ALL of your
<b>Corpses</b> as 1/1 Risen Golems
with <b>Rush</b>. For each that can't
fit, give one +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1