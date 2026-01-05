"""Effect for Improve Morale (DAL_769).

Card Text: [x]Deal $1 damage
to a minion.
If it survives, add a
<b>Lackey</b> to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)