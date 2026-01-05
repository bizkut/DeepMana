"""Effect for Mulchmuncher (BOT_523).

Card Text: <b>Rush</b>. Costs (1) less for each friendly Treant that died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass