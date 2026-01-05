"""Effect for Rotten Apple (EDR_482).

Card Text: Restore #12 Health to your hero. For the
next 2 turns, deal $3 damage to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 12, source)