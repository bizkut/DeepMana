"""Effect for Shambling Chow (NX2_024).

Card Text: <b>Rush</b>
<b>Deathrattle:</b> Deal 4 damage to your hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)