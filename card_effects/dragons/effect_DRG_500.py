"""Effect for Molten Breath (DRG_500).

Card Text: [x]Deal $5 damage to a
minion. If you're holding
a Dragon, gain 5 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)