"""Effect for Primordial Protector (BAR_042).

Card Text: [x]<b>Battlecry:</b> Draw your
highest Cost spell.
Summon a random minion
with the same Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)