"""Effect for Crystal Power (DAL_350).

Card Text: <b>Choose One -</b> Deal $2 damage to a minion; or Restore #5 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)