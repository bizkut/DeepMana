"""Effect for Rats of Extraordinary Size (SW_320).

Card Text: [x]Summon seven 1/1
Rats. Any that can't fit
on the battlefield go to
your hand with +4/+4.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_320t")