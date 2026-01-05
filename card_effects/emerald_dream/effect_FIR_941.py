"""Effect for Searing Reflection (FIR_941).

Card Text: Draw a minion. Summon an 8/8 copy of it with <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(8)