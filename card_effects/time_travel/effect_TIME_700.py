"""Effect for Chronological Aura (TIME_700).

Card Text: At the end of your turn, summon a 3/5 Dragon with <b>Taunt</b>.
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_700t")