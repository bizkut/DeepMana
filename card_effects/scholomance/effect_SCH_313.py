"""Effect for Wretched Tutor (SCH_313).

Card Text: <b>Spellburst:</b> Deal 2 damage to all other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)