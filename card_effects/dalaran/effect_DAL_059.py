"""Effect for Dimensional Ripper (DAL_059).

Card Text: Summon 2 copies of a minion in your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_059t")