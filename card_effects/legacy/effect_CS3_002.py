"""Effect for Ritual of Doom (CS3_002).

Card Text: Destroy a friendly minion. If you had 5 or more, summon a
5/5 Demon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CS3_002t")