"""Effect for Petting Zoo (DMF_086).

Card Text: Summon a 3/3 Strider. Repeat for each <b>Secret</b> you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_086t")