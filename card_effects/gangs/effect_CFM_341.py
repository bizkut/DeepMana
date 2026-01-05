"""Effect for Sergeant Sally (CFM_341).

Card Text: <b>Deathrattle:</b> Deal damage equal to this minion's Attack to all enemy minions.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 1, source)