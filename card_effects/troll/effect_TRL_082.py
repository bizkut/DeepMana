"""Effect for Big Bad Voodoo (TRL_082).

Card Text: Give a friendly minion "<b>Deathrattle:</b> Summon a random minion that costs (1) more."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_082t")