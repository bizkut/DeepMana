"""Effect for The Fist of Ra-den (YOD_042).

Card Text: [x]After you cast a spell,
summon a <b>Legendary</b>
minion of that Cost.
Lose 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_042t")