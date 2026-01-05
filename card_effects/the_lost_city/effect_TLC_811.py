"""Effect for Archaios (TLC_811).

Card Text: [x]Whenever another
friendly minion attacks,
set its Health equal to
this minion's Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)