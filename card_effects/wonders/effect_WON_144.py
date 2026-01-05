"""Effect for Eyestalk of C'Thun (WON_144).

Card Text: [x]<b>Taunt</b>, <b>Lifesteal</b>
Whenever your C'Thun gains
Attack or Health, this does
too <i>(wherever it is)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)