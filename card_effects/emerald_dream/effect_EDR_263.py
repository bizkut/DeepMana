"""Effect for Grace of the Greatwolf (EDR_263).

Card Text: [x]<b>Choose One -</b> Deal $4
damage to the enemy
hero; or Summon two
3/2 Wolves with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)