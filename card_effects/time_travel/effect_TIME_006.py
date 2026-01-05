"""Effect for Mirror Dimension (TIME_006).

Card Text: Summon a 0/4 minion with <b>Taunt</b>. If you are holding a Dragon, summon another.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_006t")