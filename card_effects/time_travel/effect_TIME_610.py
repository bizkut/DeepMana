"""Effect for Shadows of Yesterday (TIME_610).

Card Text: <b>Rewind</b>
Summon four 3/2 Shades. They each gain two
random <b>Bonus Effects</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_610t")