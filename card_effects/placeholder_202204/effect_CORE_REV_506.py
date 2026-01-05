"""Effect for Sinful Brand (CORE_REV_506).

Card Text: [x]Brand an enemy minion.
Whenever it takes
damage, deal 1 damage
to the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)