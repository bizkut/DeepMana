"""Effect for Wrathspike Brute (BT_510).

Card Text: [x]<b>Taunt</b>
After this is attacked,
deal 1 damage to
all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)