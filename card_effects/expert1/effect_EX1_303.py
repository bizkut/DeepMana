"""Effect for Shadowflame (EX1_303).

Card Text: Destroy a friendly minion and deal its Attack damage to all enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 1, source)