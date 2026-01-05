"""Effect for Wartbringer (TRL_522).

Card Text: <b>Battlecry:</b> If you played 2 spells this turn, deal 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)