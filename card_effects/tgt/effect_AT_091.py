"""Effect for Tournament Medic (AT_091).

Card Text: <b>Inspire:</b> Restore #2 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)