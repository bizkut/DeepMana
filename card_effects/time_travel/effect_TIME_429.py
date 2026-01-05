"""Effect for Divine Augur (TIME_429).

Card Text: [x]<b>Battlecry:</b> Set the Attack
and Health of every minion
in your hand to the higher
of the two stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)