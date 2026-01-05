"""Effect for Wicked Stab (Rank 1) (BAR_319).

Card Text: Deal $2 damage. <i>(Upgrades when you have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)