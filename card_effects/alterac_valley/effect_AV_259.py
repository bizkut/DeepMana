"""Effect for Frostbite (AV_259).

Card Text: Deal $3 damage.
<b>Honorable Kill:</b> Your opponent's next spell costs (2) more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)