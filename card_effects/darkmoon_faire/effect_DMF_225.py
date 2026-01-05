"""Effect for Throw Glaive (DMF_225).

Card Text: Deal $2 damage to a minion. If it dies, add a <b>Temporary</b> copy of this to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)