"""Effect for Explosive Trap (VAN_EX1_610).

Card Text: <b>Secret:</b> When your hero is attacked, deal $2 damage to all enemies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)