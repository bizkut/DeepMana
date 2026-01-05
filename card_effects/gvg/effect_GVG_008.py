"""Effect for Lightbomb (GVG_008).

Card Text: Deal damage to each minion equal to its Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)