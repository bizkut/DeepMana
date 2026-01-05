"""Effect for Flanking Maneuver (AV_269).

Card Text: Summon a 4/2 Demon with <b>Rush</b>. If it dies this turn, summon another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_269t")