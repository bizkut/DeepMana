"""Effect for Story of Umbra (DINO_415).

Card Text: [x]<b>Discover</b> a <b>Deathrattle</b>
minion that costs (5) or
more. Summon it and
trigger its <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DINO_415t")