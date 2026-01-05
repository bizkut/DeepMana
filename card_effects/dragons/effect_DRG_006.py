"""Effect for Corrosive Breath (DRG_006).

Card Text: [x]Deal $3 damage to a
minion. If you're holding
a Dragon, it also hits
the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)