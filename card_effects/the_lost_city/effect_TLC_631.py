"""Effect for Unleash the Colossus (TLC_631).

Card Text: <b>Quest:</b> Deal exactly 2 damage to an enemy
on your turn, 12 times.
<b>Reward:</b> Gorishi Colossus.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)