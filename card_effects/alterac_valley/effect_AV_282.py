"""Effect for Build a Snowman (AV_282).

Card Text: Summon a 3/3
Snowman that <b>Freezes</b>.
Add "Build a Snowbrute"
to your hand. 
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_282t")