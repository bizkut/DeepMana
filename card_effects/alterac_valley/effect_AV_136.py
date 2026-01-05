"""Effect for Kobold Taskmaster (AV_136).

Card Text: [x]<b>Battlecry:</b> Add 2
Armor Scraps to your hand
that give +2 Health to
a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)