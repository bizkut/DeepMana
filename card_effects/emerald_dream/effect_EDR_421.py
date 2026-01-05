"""Effect for Omen (EDR_421).

Card Text: [x]<b>Rush</b>, <b>Windfury</b>
<b>Deathrattle:</b> Deal 1 damage
to all enemies. <i>(Improves
after this attacks!)</i>
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)