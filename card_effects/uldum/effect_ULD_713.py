"""Effect for Swarm of Locusts (ULD_713).

Card Text: Summon seven 1/1 Locusts with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_713t")