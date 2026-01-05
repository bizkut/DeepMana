"""Effect for Furious Felfin (BT_496).

Card Text: [x]<b>Battlecry:</b> If your hero
attacked this turn, gain
+1 Attack and <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1