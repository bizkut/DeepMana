"""Effect for Whispers of the Deep (TSC_211).

Card Text: [x]<b>Silence</b> a friendly minion,
then deal damage equal to
its Attack randomly split
among all enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 1, source)