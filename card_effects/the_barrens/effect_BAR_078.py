"""Effect for Blademaster Samuro (BAR_078).

Card Text: [x]<b>Rush</b>
<b>Frenzy:</b> Deal damage equal
to this minion's Attack
 to all enemy minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 1, source)