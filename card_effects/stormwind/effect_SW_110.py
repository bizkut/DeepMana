"""Effect for Ignite (SW_110).

Card Text: Deal $2 damage. Shuffle an Ignite into
your deck that deals
one more damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)