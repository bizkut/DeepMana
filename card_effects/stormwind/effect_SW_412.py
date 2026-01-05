"""Effect for SI:7 Extortion (SW_412).

Card Text: <b>Tradeable</b>
Deal $3 damage to an undamaged character.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)