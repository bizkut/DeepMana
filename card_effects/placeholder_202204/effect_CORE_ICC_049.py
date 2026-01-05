"""Effect for Toxic Arrow (CORE_ICC_049).

Card Text: Deal $2 damage to a minion. If it survives, give it <b>Poisonous</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)