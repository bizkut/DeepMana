"""Effect for Holy Fire (EX1_624).

Card Text: Deal $5 damage. Restore #5 Health to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)