"""Effect for Ancestral Spirit (CS2_038).

Card Text: Give a minion "<b>Deathrattle:</b> Resummon this minion."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CS2_038t")