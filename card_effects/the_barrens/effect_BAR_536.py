"""Effect for Living Seed (Rank 1) (BAR_536).

Card Text: Draw a Beast. Reduce its Cost by (1). <i>(Upgrades when you
have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)