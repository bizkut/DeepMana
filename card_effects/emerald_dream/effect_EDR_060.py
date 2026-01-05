"""Effect for Ward of Earth (EDR_060).

Card Text: Gain 5 Armor. Summon a random 5-Cost minion and give it <b>Taunt</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_060t")