"""Effect for Bloodbloom (UNG_832).

Card Text: The next spell you cast this turn costs Health instead of Mana.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)