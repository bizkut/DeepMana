"""Effect for Rapid Fire (DAL_373).

Card Text: <b>Twinspell</b>
Deal $2 damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)