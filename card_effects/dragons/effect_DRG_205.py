"""Effect for Nether Breath (DRG_205).

Card Text: Deal $2 damage.
If you're holding a Dragon, deal $4 damage with <b>Lifesteal</b> instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)