"""Effect for Chatty Bartender (CORE_REV_513).

Card Text: [x]At the end of your turn,
if you control a <b>Secret</b>,
deal 2 damage to
all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)