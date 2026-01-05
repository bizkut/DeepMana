"""Effect for Gaia, the Techtonic (TSC_029).

Card Text: [x]<b>Colossal +2</b>
After a friendly Mech
attacks, deal 1 damage
to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)