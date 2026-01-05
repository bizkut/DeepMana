"""Effect for Raise Dead (SCH_514).

Card Text: Deal $3 damage to your hero. Return two friendly minions that died this game to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)