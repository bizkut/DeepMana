"""Effect for Brittlebone Destroyer (SCH_513).

Card Text: [x]<b>Battlecry:</b> If your hero's
Health changed this turn,
destroy a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()