"""Effect for Aegis of Light (EDR_264).

Card Text: Summon a random
2-Cost minion and
give it <b>Taunt</b>. <b>Imbue</b>
your Hero Power.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_264t")