"""Effect for Beaming Sidekick (ULD_191).

Card Text: <b>Battlecry:</b> Give a friendly minion +2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)