"""Effect for Bash (AT_064).

Card Text: Deal $3 damage.
Gain 3 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)