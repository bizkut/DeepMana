"""Effect for Burden of Pride (REV_334).

Card Text: [x]Summon three 1/3
Jailers with <b>Taunt</b>. If you
have 20 or less Health,
give them +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_334t")