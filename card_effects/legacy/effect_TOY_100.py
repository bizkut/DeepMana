"""Effect for Gnomelia, S.A.F.E. Pilot (TOY_100).

Card Text: [x]<b>Rush</b>. Also damages minions
next to whomever this attacks.
<b>Deathrattle:</b> Deal 2 damage
to all enemies.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)