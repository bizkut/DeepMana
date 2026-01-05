"""Effect for Healing Rain (LOOT_373).

Card Text: Restore #12 Health randomly split among all friendly characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 12, source)