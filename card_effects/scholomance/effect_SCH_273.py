"""Effect for Ras Frostwhisper (SCH_273).

Card Text: At the end of your turn,
deal $1 damage to all enemies <i>(improved by <b>Spell Damage</b>)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)