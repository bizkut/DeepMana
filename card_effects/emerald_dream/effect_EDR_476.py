"""Effect for Moonwell (EDR_476).

Card Text: Deal $4 damage to all enemy characters. Restore #4 Health to all friendly characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 4, source)