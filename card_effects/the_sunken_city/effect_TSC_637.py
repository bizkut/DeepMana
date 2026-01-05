"""Effect for Scalding Geyser (TSC_637).

Card Text: [x]Deal $2 damage.
<b>Dredge</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)