"""Effect for Death Metal Knight (CORE_ETC_523).

Card Text: [x]<b>Taunt</b>
Costs Health instead
of Mana if your hero was
healed this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)