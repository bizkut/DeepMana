"""Effect for Lava Shock (BRM_011).

Card Text: Deal $2 damage.
Unlock your <b>Overloaded</b> Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)