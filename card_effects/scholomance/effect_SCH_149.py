"""Effect for Argent Braggart (SCH_149).

Card Text: [x]<b>Battlecry:</b> Set this minion's
Attack and Health to the
highest in the battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)