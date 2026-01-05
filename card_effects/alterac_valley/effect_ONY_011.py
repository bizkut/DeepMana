"""Effect for Don't Stand in the Fire! (ONY_011).

Card Text: Deal $10 damage randomly split among all enemy minions. <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 10, source)