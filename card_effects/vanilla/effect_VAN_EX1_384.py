"""Effect for Avenging Wrath (VAN_EX1_384).

Card Text: Deal $8 damage randomly split among all enemy characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 8, source)