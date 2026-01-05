"""Effect for Lesser Jasper Spellstone (LOOT_051).

Card Text: Deal $2 damage to a minion. <i>(Gain 3 Armor to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)