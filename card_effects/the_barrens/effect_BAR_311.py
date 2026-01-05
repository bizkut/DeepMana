"""Effect for Devouring Plague (BAR_311).

Card Text: [x]<b>Lifesteal</b>. Deal $4 damage
randomly split among
all enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 4, source)