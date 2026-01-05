"""Effect for Priest of An'she (BAR_313).

Card Text: <b>Taunt</b>. <b>Battlecry:</b> If you've restored Health this turn, gain +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)