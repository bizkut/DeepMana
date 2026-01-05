"""Effect for Tidal Surge (UNG_817).

Card Text: <b>Lifesteal</b>
Deal $5 damage to a minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)