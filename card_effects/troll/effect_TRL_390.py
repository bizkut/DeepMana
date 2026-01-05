"""Effect for Daring Fire-Eater (TRL_390).

Card Text: <b>Battlecry:</b> Your next Hero Power this turn deals 2 more damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)