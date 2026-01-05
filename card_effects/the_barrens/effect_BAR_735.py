"""Effect for Xyrella (BAR_735).

Card Text: <b>Battlecry:</b> If you've restored Health this turn, deal that much damage to all enemy minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 1, source)