"""Effect for Charged Hammer (WON_321).

Card Text: <b>Deathrattle:</b> Your Hero Power becomes 'Deal 2 damage.'
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)