"""Effect for Elemental Destruction (AT_051).

Card Text: Deal $4-$5 damage to all minions. <b>Overload:</b> (2)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)