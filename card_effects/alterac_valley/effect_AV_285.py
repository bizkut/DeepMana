"""Effect for Full-Blown Evil (AV_285).

Card Text: Deal $5 damage randomly split among
all enemy minions. Repeatable this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 5, source)