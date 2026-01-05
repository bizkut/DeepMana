"""Effect for Eye Beam (BT_801).

Card Text: <b>Lifesteal</b>. Deal $3 damage to a minion.
<b>Outcast:</b> This costs (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)