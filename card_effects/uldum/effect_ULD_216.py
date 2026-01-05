"""Effect for Puzzle Box of Yogg-Saron (ULD_216).

Card Text: Cast 10 random spells <i>(targets chosen randomly).</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass