"""Effect for The Darkness (LOOT_526).

Card Text: [x]Starts <b>Dormant</b>.
<b>Battlecry:</b> Shuffle 3 Candles
into the enemy deck. When
drawn, this awakens.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)