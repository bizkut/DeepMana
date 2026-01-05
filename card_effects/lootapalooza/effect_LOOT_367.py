"""Effect for Drywhisker Armorer (LOOT_367).

Card Text: <b>Battlecry:</b> For each enemy minion, gain 2 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(2)