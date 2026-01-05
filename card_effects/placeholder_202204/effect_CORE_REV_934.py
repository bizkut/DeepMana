"""Effect for Decimator Olgra (CORE_REV_934).

Card Text: [x]<b>Battlecry:</b> Gain +1/+1
for each damaged minion,
 then attack all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1