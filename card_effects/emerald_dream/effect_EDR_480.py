"""Effect for Goldrinn (EDR_480).

Card Text: <b>Rush</b>
Friendly Beasts deal
double damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)