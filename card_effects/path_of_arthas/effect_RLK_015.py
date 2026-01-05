"""Effect for Howling Blast (RLK_015).

Card Text: [x]Deal $3 damage to an
enemy and <b>Freeze</b> it.
Deal $1 damage to all
other enemies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 3, source)