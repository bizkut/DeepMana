"""Effect for Protect the Innocent (AV_342).

Card Text: Summon a 5/5 Defender with <b>Taunt</b>. If your hero was healed this turn, summon another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_342t")