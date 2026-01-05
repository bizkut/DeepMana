"""Effect for Void Shard (SW_442).

Card Text: <b>Lifesteal</b>
Deal $4 damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)