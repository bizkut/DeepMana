"""Effect for Dreamway Guardians (DAL_733).

Card Text: Summon two 1/2 Dryads with <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DAL_733t")