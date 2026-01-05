"""Effect for Starfall (NEW1_007).

Card Text: <b>Choose One -</b>
Deal $5 damage to a minion; or $2 damage to all enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 5, source)