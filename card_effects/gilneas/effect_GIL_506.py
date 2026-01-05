"""Effect for Cheap Shot (GIL_506).

Card Text: <b>Echo</b>
 Deal $2 damage to a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)