"""Effect for Cyclopian Horror (OG_337).

Card Text: <b>Taunt</b>. <b>Battlecry:</b> Gain      +1 Health for each enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)