"""Effect for Arcane Breath (DRG_106).

Card Text: Deal $2 damage to a minion. If you're holding a Dragon, <b>Discover</b> a spell.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)