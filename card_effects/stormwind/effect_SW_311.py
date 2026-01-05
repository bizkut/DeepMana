"""Effect for Garrote (SW_311).

Card Text: [x]Deal $2 damage to the
enemy hero. Shuffle 3
Bleeds into your deck that
deal $2 more when drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)