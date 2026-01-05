"""Effect for Ray of Frost (DAL_577).

Card Text: <b>Twinspell</b>
<b>Freeze</b> a minion.
If it's already <b>Frozen</b>,
deal $2 damage to it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)