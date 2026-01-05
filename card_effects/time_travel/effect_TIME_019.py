"""Effect for Manifested Timeways (TIME_019).

Card Text: <b>Battlecry:</b> If you control
an Aura, deal 3 damage
to all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)