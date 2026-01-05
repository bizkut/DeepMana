"""Effect for Firebrand (SCH_241).

Card Text: <b><b>Spellburst</b>:</b> Deal 4 damage randomly split among all enemy minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 4, source)