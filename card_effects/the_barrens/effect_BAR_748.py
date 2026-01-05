"""Effect for Varden Dawngrasp (BAR_748).

Card Text: [x]<b>Battlecry:</b> <b>Freeze</b> all enemy
minions. If any are already
<b>Frozen</b>, deal 4 damage
to them instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 4, source)