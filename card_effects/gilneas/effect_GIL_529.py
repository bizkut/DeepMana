"""Effect for Spellshifter (GIL_529).

Card Text: [x]<b>Spell Damage +1</b>
Each turn this is in your hand,
swap its Attack and Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)