"""Effect for Frozen Touch (REV_601).

Card Text: Deal $3 damage.
<b>Infuse (3):</b> Add a Frozen Touch to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)