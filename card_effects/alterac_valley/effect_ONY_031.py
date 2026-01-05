"""Effect for Smokescreen (ONY_031).

Card Text: [x]Draw 5 cards. Trigger
any <b>Deathrattles</b> drawn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)