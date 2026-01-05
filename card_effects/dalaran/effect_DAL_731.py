"""Effect for Duel! (DAL_731).

Card Text: Summon a minion from each player's deck.
They fight!
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_731t")