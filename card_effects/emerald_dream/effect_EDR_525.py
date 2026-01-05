"""Effect for Barbed Thorn (EDR_525).

Card Text: [x]<b>Choose One -</b> Gain
<b>Poisonous</b> this turn; or Gain
"<b>Deathrattle:</b> Deal 2 damage
to all enemies."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)