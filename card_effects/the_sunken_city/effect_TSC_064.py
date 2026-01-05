"""Effect for Slithering Deathscale (TSC_064).

Card Text: <b>Battlecry:</b> If you've cast three spells while holding this, deal 3 damage to all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)