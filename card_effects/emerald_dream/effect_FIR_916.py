"""Effect for Smoldering Ascent (FIR_916).

Card Text: Deal ${0} damage to all enemy minions. <i>(Upgrades each turn,
but discards after {1}!)</i>1Deal ${0} damage to all enemy minions.
<i>(Discards this turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 0, source)