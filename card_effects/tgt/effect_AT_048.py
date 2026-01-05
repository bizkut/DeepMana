"""Effect for Healing Wave (AT_048).

Card Text: Restore #8 Health. Reveal a minion in each deck. If yours costs more, restore #16 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)