"""Effect for Memoriam Manifest (TIME_616).

Card Text: Summon the highest Cost friendly Undead that died this game.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_616t")