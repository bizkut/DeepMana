"""Effect for Stormpike Aid Station (AV_664).

Card Text: [x]At the end of your turn,
give your minions +2
Health. Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)